import json
import jmespath

# First image
with open('air_bnb.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('air_bnb2.json','r',encoding='utf-8')as f:
    snd_data = json.load(f)

with open('airbnb_review.json','r',encoding='utf-8') as f:
    review= json.load(f)
rest_name = "niobeClientData[0][1].data.presentation.stayProductDetailPage.sections.sections[21].section.listingTitle"
rest_res = jmespath.search(rest_name,data).split("|")[2].strip()
# print(rest_res)
Hotel_name = "niobeClientData[].data.presentation.stayProductDetailPage.sections.sbuiData.sectionConfiguration.root[].sections[0].sectionData.title"
Host_name = "niobeClientData[].data.presentation.stayProductDetailPage.sections.sbuiData.sectionConfiguration.root[].sections[1].sectionData.title"
result = jmespath.search(Hotel_name, data)
host_result = jmespath.search(Host_name, data)

rooms = "niobeClientData[].data.presentation.stayProductDetailPage.sections.sbuiData.sectionConfiguration.root[].sections[].sectionData.overviewItems[].title"
rooms_result = jmespath.search(rooms, data)
# print(rooms_result)
d1 = {}
for i in rooms_result:
    temp = i.split(" ")
    d1[f"{temp[1]}"] = int(temp[0])
   

# print(d1)


rating = "niobeClientData[].data.presentation.stayProductDetailPage.sections.sections[].section.heading.title"
rating_result = jmespath.search(rating, data)


highlights_title = "niobeClientData[].data.presentation.stayProductDetailPage.sections.sections[].section.highlights[].title"
high_result = jmespath.search(highlights_title, data)

highlights_subtitle = "niobeClientData[].data.presentation.stayProductDetailPage.sections.sections[].section.highlights[].subtitle"
sub_result = jmespath.search(highlights_subtitle, data)
# print(sub_result)

item_text = "niobeClientData[].data.presentation.stayProductDetailPage.sections.sections[].section.items[].html.htmlText"
itmtxt_result = jmespath.search(item_text, data)


# check-in check-out details
title = "data.presentation.stayProductDetailPage.sections.sections[].section.initialPill.title"
title_result = jmespath.search(title, snd_data)
# print(title_result)

firstPart_bnb2 = jmespath.search("data.presentation.stayProductDetailPage.sections.sections[1].section.structuredDisplayPrice.primaryLine",snd_data)
# print(firstPart_bnb2)

paymentDetails = {"currency":'INR',"discounted_price":int(firstPart_bnb2.get("discountedPrice")[1:].replace(",","")),"original_price":int(firstPart_bnb2.get("originalPrice")[1:].replace(",","")),"price_type":firstPart_bnb2.get("qualifier")}
# print(paymentDetails)





# second image


place_offer ="niobeClientData[].data.presentation.stayProductDetailPage.sections[].sections[20].section.title"
title_result = jmespath.search(place_offer,data)

ofer ="niobeClientData[].data.presentation.stayProductDetailPage.sections[].sections[20].section[].previewAmenitiesGroups[].amenities[].title"
of_result = jmespath.search(ofer,data)

all_ofer ="niobeClientData[].data.presentation.stayProductDetailPage.sections[].sections[20].section[].seeAllAmenitiesGroups[].title"
of_result = jmespath.search(all_ofer,data)
ofer_ameni ="niobeClientData[].data.presentation.stayProductDetailPage.sections[].sections[].section.seeAllAmenitiesGroups[].{group: title,items: amenities[].title}"
ame_result = jmespath.search(ofer_ameni,data)

amenities_dict = {}

for g in ame_result:          # ame_result is your list
    group_name = g.get("group")
    items = g.get("items", [])

    if group_name:
        amenities_dict[group_name] = items

# print(amenities_dict)

# Third image
name = "niobeClientData[].data.presentation.stayProductDetailPage.sections[].sections[5].section.cardData.name"
res= jmespath.search(name,data)
# print(res)

stat = "niobeClientData[].data.presentation.stayProductDetailPage.sections[].sections[5].section.cardData[].stats[].value"
stat_res= jmespath.search(stat,data)

label = "niobeClientData[].data.presentation.stayProductDetailPage.sections[].sections[5].section.cardData[].stats[].label"
lbl_res= jmespath.search(label,data)
# print(lbl_res)



# fourth image

firstname = "data.presentation.stayProductDetailPage.reviews.reviews[].reviewer.firstName"
n_res = jmespath.search(firstname,review)
# print(n_res)

rew_rating = "data.presentation.stayProductDetailPage.reviews.reviews[].rating"
r_res = jmespath.search(rew_rating,review)
# print(r_res)

date = "data.presentation.stayProductDetailPage.reviews.reviews[].localizedDate"
d_res = jmespath.search(date,review)
# print(d_res)

comment = "data.presentation.stayProductDetailPage.reviews.reviews[].commentV2"
c_res = jmespath.search(comment,review)
# print(c_res)

profileView = {
    "host_name": res[0],
    "details": dict(zip(
        lbl_res,
        [float(v) if '.' in v else int(v) for v in stat_res]
    ))
}

reviews_list = []
for name, rating, date, comment in zip(n_res, r_res, d_res, c_res):
    reviews_list.append({
        "reviewer_name": name,
        "rating": rating,
        "date": date,
        "comment": comment
    })
final_output = {
    "restaurantsname":rest_res,
    "details":{
        "title": result,
        "rooms": d1,
        "rating": rating_result,
        "highlights": {
            "titles": high_result,
            "subtitles": sub_result
        },
        "description_items": itmtxt_result,
        "checkin_checkout_titles": title_result,
        
    },
    "pricing": paymentDetails,
        "amenities": amenities_dict,
        "reviews": reviews_list,
        "profileView": profileView

}

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=4, ensure_ascii=False)