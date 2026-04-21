from request import request 
import json
from lxml import html
from urllib.parse import urljoin
import requests as re
from concurrent.futures import ThreadPoolExecutor
from db import *

create_movies_table()
base_url = "https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest?page={}"

for page in range(1, 4):
    url = base_url.format(page)
    data = request(url)
   
    
    with open("movie.html",'w',encoding='utf-8') as f:
        f.write(data)


    
    tree = html.fromstring(data)
    script_data = tree.xpath("//script[@type = 'application/ld+json']/text()")

    for s in script_data:
        script = json.loads(s)

def find_url(url):
    res = re.get(url)
    all_json = json.loads(res.text)

    return all_json     
    
movie_link = tree.xpath("//div[contains(@class , 'flex-container ')]//a/@href")

def extract_ld_json(url):
    data = request(url)
    if not data:
        return None

    tree = html.fromstring(data)
    return tree

all_href=[]

for m in movie_link:
    href=urljoin(base_url,m)
    all_href.append(href)  

def process(d):
    try:
        tree = extract_ld_json(d)
        if tree is None:
            return None

        def sx(path):
            return tree.xpath(f"string({path})").strip()

        name = sx("//h1")
        score = sx("//rt-text[@slot='critics-score']") or "0%"
        reviews_count = sx("//rt-link[@slot='critics-reviews']")
        desc = sx("//div[@slot='description']//rt-text")
        img = sx("//img[@slot='poster']/@src")
        want_to_know = sx("//div[@id='critics-consensus']//p")

        cast_crew =[]
        all_reviews= []
        videos = []

        cast_href = urljoin(base_url,sx("string(//section[@aria-labelledby='cast-and-crew-label']//rt-button/@href)").strip())
        if cast_href:
            cast_page = extract_ld_json(urljoin(base_url, cast_href))
            if cast_page is not None:
                for c in cast_page.xpath("//cast-and-crew-card"):
                    cast_crew.append({
                        "name": c.xpath("string(.//rt-text[@slot='title'])").strip() or None,
                        "character": c.xpath("string(.//rt-text[@slot='characters'])").strip() or None,
                        "role": c.xpath("string(.//rt-text[@slot='credits'])").strip() or None,
                        "url": urljoin(base_url, c.xpath("string(@media-url)").strip()) if c.xpath("@media-url") else None
                    })
        # print("cast ",cast_href)
        json_obj = tree.xpath("//script[@data-json='props']/text()")
        if json_obj:
            props = json.loads(json_obj[0])
            emsId = (props.get("vanity") or {}).get("emsId")

            if emsId:
                review_url = f"https://www.rottentomatoes.com/napi/rtcf/v1/movies/{emsId}/reviews?type=critic"
                review_data = find_url(review_url)

                for r in review_data.get("reviews", []):
                    all_reviews.append({
                        "name": r.get("critic", {}).get("displayName"),
                        "review": r.get("reviewQuote"),
                        "count": r.get("originalScore"),
                        "review_type": r.get("scoreSentiment")
                    })
        # print("all reviews",props)
        
        video_href = sx("//rt-button[@data-qa='videos-view-all-link']/@href")
        if video_href:
            video_page = extract_ld_json(urljoin(base_url, video_href))
            if video_page is not None:
                for v in video_page.xpath("//div[@data-qa='video-item']"):
                    videos.append({
                        "title": v.xpath("string(.//a[@data-qa='video-item-title'])").strip(),
                        "url": urljoin(base_url, v.xpath("string(.//a/@href)").strip()),
                        "duration": v.xpath("string(.//span[@data-qa='video-item-duration'])").strip(),
                        "thumbnail": v.xpath("string(.//img/@src)").strip()
                    })

        # print("Done:", name)

        return {
            "name": name,
            "score": score,
            "reviews_count": reviews_count,
            "description": desc,
            "poster": img,
            "critics_consensus": want_to_know,
            "cast_crew": cast_crew,
            "reviews": all_reviews,
            "videos": videos
        }

    except Exception as e:
        print("Error in process:", e)
        return None

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(process, all_href)

    for r in results:
        if not r:
            continue

        if not r.get("name"):
            print("Skipping empty record")
            continue

        insert_movie(r)

