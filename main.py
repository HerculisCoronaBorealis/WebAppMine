
import requests
from flask import Flask, request, jsonify
from flask.templating import render_template
import random
import json
import queue
import time
import threading
app = Flask(__name__, template_folder='template')
app.secret_key = "KarmaBeast"

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': 'C=0; O=0; V=fe1e774898a9e7b65927f05535ada8705f152e752524b9.90528389; optimizelyEndUserId=oeu1595223668906r0.027934908966102512; s_ecid=MCMID%7C60185159885597638692678916017568026992; _pxvid=9e914527-ca4b-11ea-873f-0242ac120007; _scid=c0e2ac1b-c16f-427c-b8f8-27515740bc3a; _ga=GA1.2.393893998.1595223673; _fbp=fb.1.1595223672826.978579793; _gcl_au=1.1.1989468470.1595223673; LPVID=NhNDcyZGRlM2VkZTc0NWIw; capp_promo_modal_shown=true; chgcsdetaintoken=1; _cs_c=1; gidr=MA; _fbc=fb.1.1599969124642.IwAR2Z_VnbjqNnsD1ZSHBH6JBGIt6Y8vleePHePlIWV46T8HrySaTg-TJC5d8; __gads=ID=f883ea08ff0a1d81:T=1595379471:R:S=ALNI_MaBxxG4YtrOaiGu_1x6Ac4NFu2MQw; gid=1565479; _rdt_uuid=1595423827407.d4ba5f79-eb95-42cb-99df-4fe73a0751ec; uuid230=d9d0fb2e-1924-4184-9188-aefa161dffe3; al_cell=main-1-control; _ym_uid=1614747935772498421; _ym_d=1614747935; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Atrue%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Atrue%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%7D; chgcsastoken=UWnWQm7kp32N_fR_Bl2RF-x7iHNErEbx898rP3W5R4qJd8i8zH_8RUngGZXvUqDbF5vJDQAcTpwrTcpQPYFLWmJ6ugip8PiORojxbW-VSV897aeI-UJYvuxB2DGceKC3; _gac_UA-499838-3=1.1617246489.CjwKCAjwu5CDBhB9EiwA0w6sLVoBK3rSmbC5yrXC8GVwB9gv4eZqVBsE6Mg4wzBSTZFvjgJgt_yf8RoCHN8QAvD_BwE; _gcl_aw=GCL.1617246492.CjwKCAjwu5CDBhB9EiwA0w6sLVoBK3rSmbC5yrXC8GVwB9gv4eZqVBsE6Mg4wzBSTZFvjgJgt_yf8RoCHN8QAvD_BwE; _gcl_dc=GCL.1617246492.CjwKCAjwu5CDBhB9EiwA0w6sLVoBK3rSmbC5yrXC8GVwB9gv4eZqVBsE6Mg4wzBSTZFvjgJgt_yf8RoCHN8QAvD_BwE; chgmfatoken=%5B%20%22account_sharing_mfa%22%20%3D%3E%201%2C%20%22user_uuid%22%20%3D%3E%20fffd3170-ab55-4060-bb43-72e353855b73%2C%20%22created_date%22%20%3D%3E%202021-05-09T09%3A23%3A55.825Z%20%5D; U=50fb2356a4bd17ca93c19bc804c2141c; id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJmZmZkMzE3MC1hYjU1LTQwNjAtYmI0My03MmUzNTM4NTViNzMiLCJhdWQiOiJDSEdHIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsImV4cCI6MTYzNzE2NTM1NywiaWF0IjoxNjIxMzk1MzU3LCJlbWFpbCI6ImthdHJpbmEua2FsZUBhb2wuY29tIn0.nkd_VoRQWdORVK3uaHdStSPJPTOQw0gtoJi06iE-s-dICTUwsN7LIUhYU8TNjrm0kE7AdwhLlJFwkmaXxaUava0DUtddOrRTWPQ0Iq6ZFcBgtEFj8dGwIyMio3MIBIra77iX33f-eSVqBEDdgGtt_h5Q0yknXLmC5PYfe0GLVQPWIAvSvlE6HpK2SFukJLG4l-wQogTS4zYP7UJ6b247uhdvDl-L6UwcR4i5rHPWFE45SCV0Fdk7JtPU206JcVx9l03RLq8GZNI4XK9JdQ_mGWKHpJ_Yj1bMXjk6CiNJfIp4DS0VE1PhWZwk9Q45yVvedtfw2F5xPT4ujO7DuCFjWQ; _sctr=1|1621796400000; WRUID=3305402793935298; exp=A311C%7CA803B%7CA560B%7CA294C%7CA100B%7CA259B%7CA184B%7CA735B%7CC024C%7CA207A%7CA209A%7CA212A%7CA270C%7CA890H%7CA110B%7CA966C%7CA448A%7CA278C%7CA935A%7CA315B; expkey=00E1330B2980EA15068F08B99E91804A; intlPaQExitIntentModal=hide; _cs_id=6b30d022-fd86-ad2b-8d43-2d7961085730.1595392331.30.1622224873.1622224873.1.1629556331161.Lax.0; __CT_Data=gpv=102&ckp=tld&dm=chegg.com&apv_79_www33=102&cpv_79_www33=102&rpv_79_www33=5; PHPSESSID=645f3fda532bb900f26cd9f5db77d021; user_geo_location=%7B%22country_iso_code%22%3A%22PK%22%2C%22country_name%22%3A%22Pakistan%22%2C%22region%22%3A%22PB%22%2C%22region_full%22%3A%22Punjab%22%2C%22city_name%22%3A%22Bahawalpur%22%2C%22postal_code%22%3A%2263101%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22ur-PK%22%5D%7D%7D; CSessionID=5f512007-5bc6-47ec-b538-3e9f43adb24f; SU=otOdLQtSyd0OCAx2u79a6LlTVwfFqn-OMAl2fBrI07alkcn98skdaN4x60HwG0YQqOTw1o6bE-OG-ejJHVb0EpwdkGWjuHX84XonZ_G0QMVeR-MVPbwcLswgt2G0WsFr; AMCVS_3FE7CBC1556605A77F000101%40AdobeOrg=1; CVID=2f019103-d2d9-4f85-9481-a82cfe3deb56; _gid=GA1.2.1166389551.1622351555; opt-user-profile=fe1e774898a9e7b65927f05535ada8705f152e752524b9.90528389%252C19944471923%253A19956173008; OptanonConsent=isIABGlobal=false&datestamp=Sun+May+30+2021+18%3A18%3A45+GMT%2B0500+(Pakistan+Standard+Time)&version=6.10.0&hosts=&consentId=1e2fc7a1-fc85-4e09-b274-6753c9ef6c34&interactionCount=1&landingPath=NotLandingPage&groups=snc%3A1%2Cfnc%3A1%2Cprf%3A1%2CSPD_BG%3A1%2Ctrg%3A1&AwaitingReconsent=false; fffd3170-ab55-4060-bb43-72e353855b73_TMXCookie=true; _uetsid=a621fd30c10511eba2ed4f7426322bc0; _px3=77c5021a52d97ac8c402213db775910b130342d0acd4deab8078393d32463e69:qpxOFKUYYJzz/MEMQUlrQYvdynK/SDPqFzrTIun9LxGFA/PFFxR90GpnOEHmarDNZMuQ3Ge+0uozJ66P/xzccg==:1000:r9V+4HlVOuKmYqY0TVM8pjaOs3hgarkJ0vkXU5P+ZA0Vj81KBUOMBnVgWLqRzbEs6EE/LPNy3NJ9kVScWBpEOiBJ+vWVL34SsI5ThZklCn6Nm/P6hcU4aTOrKtuIFxvd3kXPgTE3/DJYxHpWk9JIVAJPJfGHuUxq4hhnw71WyiAm5q/C1rM0Q6DcY6PZzoPPpbBlLc909XzaekW6ho3nxg==; _px=qpxOFKUYYJzz/MEMQUlrQYvdynK/SDPqFzrTIun9LxGFA/PFFxR90GpnOEHmarDNZMuQ3Ge+0uozJ66P/xzccg==:1000:Y4pXjSzsOoZmu9BVlUiEqhRdjJZ0WKEPRWGgYjb0BWNRqrrHKYYgY1G+f91RiTmCFtmfaHTzIKgxGVz9wIlsvjA7zV3Nq+b0L6wi+/8tWVJRCe/D5g1Qr7fAaUzn9d9h/9BGgMcvh+jZjHmvTgQL3dYeXx2lxJLw+4dKRQxJ0C/x3obzqrT8nSXVZfX34llT3ePhjVSpo8afxzMLq3y4izWFkjVyQKtoeHqBUGNKV28fyBujMOuYAJEd5Z6I03W2vTlxSXTFOW9+RN5V+9sMBw==; s_pers=%20buFirstVisit%3Dcore%252Ccs%252Cothers%252Chelp%252Ctb%252Ccw%252Cmoney%7C1779113678163%3B%20gpv_v6%3Dno%2520value%7C1622382871339%3B; s_sess=%20buVisited%3Dcs%252Ccore%3B%20s_sq%3Dcheggincriovalidation%253D%252526pid%25253Dchegg%2525257Cweb%2525257Ccs%2525257Cchegg%25252520study%25252520homepage%252526pidt%25253D1%252526oid%25253Dfunctionqr%25252528%25252529%2525257B%2525257D%252526oidt%25253D2%252526ot%25253DDIV%3B%20s_ptc%3D%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D45D91C60C20A5CBD-1F362F14A572F674%3B; _gali=chegg-searchbox; AMCV_3FE7CBC1556605A77F000101%40AdobeOrg=-408604571%7CMCIDTS%7C18778%7CMCMID%7C60185159885597638692678916017568026992%7CMCAAMLH-1622985881%7C3%7CMCAAMB-1622985881%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1622388281s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.6.0%7CMCCIDH%7C-608999569',
    'origin': 'https://www.chegg.com',
    'pragma': 'no-cache',
    'referer': 'https://www.chegg.com/',
    "sec-ch-ua-platform": "Windows",
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}
with open('./chegg_cookies.txt', 'r') as cookies:
    chegg_cookies = cookies.read().splitlines()


def HeaderGen():
    SelectedCookie = random.choice(chegg_cookies)
    header = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'cookie': SelectedCookie,
        'origin': 'https://www.chegg.com',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36',
    }
    List = [SelectedCookie, header]
    return List


def newlikeIt(link, cookie):
    # try:
    print("I'm in")
    header = {
        'authority': 'atc-edge.studybreakmedia.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'script',
        'referer': f'{link}',
        'cookie': f"{cookie}",
        'accept-language': 'en-US,en;q=0.9',
    }
    content = requests.get(link.replace(
        ' ', "").replace('\n', ""), headers=header).text
    open("testingResults.html", 'w', encoding='utf-8').write(content)
    askerId = content.split('data-askerId="')[1].split('"')[0]
    entityId = content.split('data-answerId="')[1].split('"')[0]
    # answerDate = content.split(
    #     'data-ansCreateDate="')[1].split('"')[0].replace(':', '%3A')
    questionId = content.split('data-qid="')[1].split('"')[0]
    answerDate = content.split('data-ansCreateDate="')[1].split('"')[0]
    token = content.split('"token":"')[1].split('"')[0]
    query = 'askerId={}&entityType=ANSWER&entityId={}&reviewType=LIKE_DISLIKE&reviewValue=0&token={}&questionId={}'.format(
            askerId, entityId, token, questionId)
    header = {
        'authority': 'www.chegg.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.chegg.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'{link}',
        'cookie': f"{cookie}",
        'accept-language': 'en-US,en;q=0.9',
    }
    query = {
        'askerId': f'{askerId}',
        'entityType': 'ANSWER',
        'entityId': f'{entityId}',
        'reviewType': 'LIKE_DISLIKE',
        'reviewValue': '0',
        'answerCreatedDate': f'{answerDate}',
        'token': f'{token}',
        'questionId': f'{questionId}'
    }
    print(query)
    try:
        liked = requests.post('https://www.chegg.com/study/_ajax/contentfeedback/savereview',
                              headers=header, data=query)
        print(liked.cookies)
        liked = liked.json()["httpCode"]
        return [200]
    except:
        print(liked.text)
        return [400]
    # except:
    # 	return [403]


def TBSHtmlGenerator(Answer, Question):
    Html = '''<html><head></head><body><div class="main">
	<h2 class="accordion active"><b>Question</b></h2>
								<div class="question">



	<div id="mobile-question-style" style="font-family: 'Helvetica Neue',Helvetica,Arial; color:#333333;">''' + '\n{}\n'.format(
        Question) + '''</div>


										</div>
								<h2 class="accordion active"><b>Answer</b></h2><div class="question">
										''' + '\n{}\n'.format(Answer) + '''</div>
				<script>
				var acc = document.getElementsByClassName("accordion");
				var i;
				for (i = 0; i < acc.length; i++) {
					acc[i].addEventListener("click", function () {
						this.nextElementSibling.classList.toggle('collapse')
						this.nextElementSibling.classList.toggle('expand')

					});
				}
			</script>
				<style>

			.img-container-block {
				text-align: center;
			}
			.img-container-inline {
				text-align: center;
				display: block;
			}
			.img-container img {
				width: 92px;
				position: absolute;
				left: 25%;
				top: 6px;
				border: 2px solid #00247;
				border-radius: 50px;
			}
			.step {
				margin: auto;
				margin-top: 7px;
				text-align: center;
				padding: 7px;
				color: #fff;
				font-size: 16px;
				background: #f78112;
				font-weight: bold;
				border-radius: 15px;
			}
			.accordion {
				background-color: #f78112;
				padding: 10px;
				font-size: 15px;
				color: white;
				border-radius: 29px;
				text-align: center;
				text-transform: uppercase;
				width: auto;
				height: auto;
				overflow: hidden;
				filter: brightness(100%);
				transition: filter 0.15s;
			}
	.ad_shadow{
				box-shadow: 0px 0px 3px 1px rgba(0,0,0,0.75);
				-webkit-box-shadow: 0px 0px 3px 1px rgba(0,0,0,0.75);
				-moz-box-shadow: 0px 0px 3px 1px rgba(0,0,0,0.75);

			}
	.ad{
				width: 18%;
				margin-right: 9px;
				border-radius: 10px;
				max-height: 92px;
			}
	.products{
		margin:10px 0px 10px 19px;
	}
			.question {
				padding: 0 10px;
				margin: 0px 35px 0px 35px;
				border-left: 12px solid;
				border-radius: 20px;
				border-top: 2px solid;
				border-right: 12px solid;
				border-bottom: 2px solid;
				border-color: #f78112;
				text-align: center;
				overflow: hidden;
			}
			.main {
				background-color: white;
			}
			</style></div></body></html>'''
    return Html


def TBS(Question, Cookie, Link):
    try:
        ChapterId = Question.split('"chapterId":"')[1].split('"')[0]
    except:
        ChapterId = Question.split("\\/?id=")[1].split('&')[0]
    try:
        likes = Question.split('"positiveReviewCount":')[1].split(',')[0]
    except:
        likes = "0"
    try:
        dislikes = Question.split('"negativeReviewCount":')[1].split('}')[0]
    except:
        dislikes = "0"
    Token = str(Question.split('"token":"')[1].split('"')[0])
    ISBN = str(Question.split('"isbn13":"')[1].split('"')[0])
    QID = str(Question.split('problemId":"')[1].split('"')[0])
    try:
        cheggheader = {
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'cookie': "{}".format(Cookie),
            'origin': 'https://www.chegg.com',
            'referer': "{}".format(Link),
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Mobile Safari/537.36',
        }
        query = {"query": {"operationName": "getSolutionDetails", "variables": {"isbn13": "{}".format(
            ISBN), "chapterId": "{}".format(ChapterId), "problemId": "{}".format(QID)}}, "token": "{}".format(Token)}
        Content = requests.post(
            'https://www.chegg.com/study/_ajax/persistquerygraphql', headers=cheggheader, data=json.dumps(query))
        json.dump(Content.json(), open("tbsSolution.json", "w"), indent=4)
        Content = Content.text.replace("\\", "")
        totalSteps = Content.split('"totalSteps":')[1].split(',')[0]
        book = Content.split('"coverName":"')[1].split('"')[0]
        edition = Content.split('"editionNumber":')[1].split(',')[0]
        bookmarks = Content.split('"userAssetCount":')[1].split(',')[0]
        chapterName = Content.split('chapterName":"')[1].split('"')[0]
        problemName = Content.split('problemName":"')[1].split('"')[0]
        print(edition)
        try:
            Question = Content.split('problemHtml":"')[1].split('","user')[
                0]
        except:
            Question = ''
        HTMlIndexes = Content.split('"html":"')
        HTMlIndexes[0] = ''
        count = 0
        Steps = ''
        for i in HTMlIndexes:
            if '<div' in i:
                count += 1
                Steps += f'''<li><section class="step TBS_SOLUTION_STEP opened" data-id="9.1-2lo-2"><h4 class="step-header" tabindex="0" role="button" aria-pressed="true"><span class="step-num">Step {count} </span><span class="step-total">of {totalSteps}</span></h4><div class="content"><div class="html step-html">{i.split('","link"')[0]}</div></section></li>'''
    except:
        Steps = '<p><span style="background-color: #ffffff; color: #ff0000; font-size: 18px;"><strong>Oh No!! No One Has Answered It Yet...</strong></span></p>'
    return {"solution": Steps.replace('class="content"', 'class="tbs_content"'), "question": Question, "likes": likes, "dislikes": dislikes, "type": "tbs", "about": f"bookmarks={bookmarks},bookName={book},editionNumber={edition},chapter={chapterName},problem={problemName}"}


def QuestionHtml(Extracted, q1):
    totalAnswers = ""
    try:
        Question = str(Extracted[Extracted.index(
            '<div class="ugc-base question-body-text">'):])
        Question = Question[:Question.index('<div class="avatar-comments')]
        Question = Question[:Question.rfind('</div>')] + "</div>"
        Question = Question.replace('"//', '"https://')
        Question = Question.replace('<img ', '<img class="Beaster" ')
        try:
            answerer = Extracted.split('"displayName":"')[1].split('"')[0]
        except:
            answerer = "Anonymous"
        totalAnswers = Extracted.split(
            "<span class='answers-total'>")[1].split('<')[0]
    except:
        Question = '<p><span style="color: #ff0000;text-align: center;display: block;"><strong>No one has Answered it yet</strong></span></p>'
    q1.put([totalAnswers, answerer, Question])


def CommentsHtml(Extracted, q3):
    try:
        Comment = Extracted.split(
            '<div class="comments-markup mod-parent-container">')
        Comment[-1] = Comment[-1].split('<div class="leave-comment ">')[0]
        Comments = ''
        for i in Comment:
            if '<span class="comment-date">' in i:
                Comments += ('<div class="comments-markup mod-parent-container">' + i)
        Comments = Comments.replace('"//', '"https://')
        if Comments == '':
            Comments = '<p><span style="color: #ff0000;text-align: center;display: block;"><strong>No one has commented it yet</strong></span></p>'
    except:
        Comments = '<p><span style="color: #ff0000;text-align: center;display: block;"><strong>No Comments</strong></span></p>'
    q3.put(Comments)


def Like_Dislike(Extracted, header, q4):
    Likes = '0'
    Dislikes = '0'
    try:
        LikID = Extracted.split('"answerId":')[1].split(',')[0]
    except:
        try:
            LikID = Extracted.split('data-answerId="')[1].split('"')[0]
        except:
            LikID = 'None'
    Like_disLike = requests.get(
        'https://www.chegg.com/study/_ajax/contentfeedback/getreview?entityType=ANSWER&entityId={}'.format(LikID), headers=header).text
    if LikID != 'None':
        for i in Like_disLike.split('}},'):
            try:
                Extract = i.split('"result":')[1]
                if len(Extract) > 10:
                    for under in Extract.split('"}'):
                        if '"reviewValue":"0' in under:
                            Likes = under.split('"count":')[1].split(',')[0]
                        elif '"reviewValue":"1' in under:
                            Dislikes = under.split('"count":')[1].split(',')[0]
            except:
                Likes = '0'
                Dislikes = '0'
    q4.put([Likes, Dislikes])


def QASolution(Extracted, q5):
    try:
        Extracted = str(Extracted[Extracted.index(
            '<div class="answer-given-body ugc-base">'):])
        Solution = str(Extracted[:Extracted.index('<a href="#"')])
        Solution = Solution.replace('"//', '"https://')
        Solution = Solution.replace('<img', '<img class="Beaster"')
    except:
        Solution = "<p><span style='color: #339966;'><strong>This question hasn't been answered yet!</strong></span></p>"
    q5.put(Solution)


def solution(Extracted, header):
    open("Died.html", "w", encoding="utf-8").write(Extracted)
    Threads = []
    q1 = queue.Queue()
    q3 = queue.Queue()
    q4 = queue.Queue()
    q5 = queue.Queue()
    Threads.append(threading.Thread(target=QuestionHtml, args=(Extracted, q1)))
    Threads.append(threading.Thread(target=CommentsHtml, args=(Extracted, q3)))
    Threads.append(threading.Thread(
        target=Like_Dislike, args=(Extracted, header, q4)))
    Threads.append(threading.Thread(target=QASolution, args=(Extracted, q5)))
    for i in Threads:
        i.start()
    try:
        QuestionHead = '<em>' + \
            Extracted.split('headline"><em>')[1].split('</h1>')[0]
    except:
        QuestionHead = '<b>Question</b>'
    for i in Threads:
        i.join()
    totalAns, Answerer, Question = q1.get()
    Comments = q3.get()
    Likes, Dislikes = q4.get()
    Solution = q5.get()
    finalJson = {"type": "qa", "solution": Solution.replace("'", '"'), "question": Question.replace("'", '"'), "likes": Likes, "dislikes": Dislikes,
                 "comments": Comments, "questionHead": QuestionHead, "expert": Answerer, "expertAns": totalAns}
    return finalJson


def ContentGrabber(url):
    Cookie, header = HeaderGen()
    Responce = requests.get(url, headers=header)
    return([Cookie, header, Responce])


def grb_det(url):
    # try:
    # 	headers = {
    # 			'authority': 'atc-edge.studybreakmedia.com',
    # 			'pragma': 'no-cache',
    # 			'cache-control': 'no-cache',
    # 			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    # 			'sec-ch-ua-mobile': '?0',
    # 					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    # 					'sec-ch-ua-platform': '"Windows"',
    # 					'accept': '*/*',
    # 					'sec-fetch-site': 'cross-site',
    # 					'sec-fetch-mode': 'no-cors',
    # 					'sec-fetch-dest': 'script',
    # 					'referer': f'{url}',
    # 					'cookie': random.choice(chegg_cookies),
    # 					'accept-language': 'en-US,en;q=0.9',
    # 		}
    # 	response = requests.get(url, headers=headers).text
    # 	open("new9111.html", "w").write(response)
    # 	question_head = response.split('<em>Question: </em>')[1].split('</h1>')[
    # 			0].replace('\\n', ' ').replace('<br>', '')
    # 	subjectName = response.split('"subSubjectName":"')[1].split('"')[0]
    # 	try:
    # 		positiveRat = response.split('"positiveAnswerReviewCount"')[
    # 			1].split('"')[0]
    # 	except:
    # 		positiveRat = "0"
    # 	try:
    # 		NegRat = response.split('"negativeAnswerReviewCount"')[
    # 			1].split('"')[0]
    # 	except:
    # 		NegRat = "0"
    # 	resp = {"code": "1", "positive": positiveRat, "negative": NegRat,
    # 				"queHead": question_head, "subjectName": subjectName}
    # 	return resp
    # except:
    # 	return {"code": "303", "text": "Invalid Chegg Link"}
    resp = {"code": "1", "positive": "0", "negative": "0",
            "queHead": url, "subjectName": "None"}
    return resp


def SolutionFinalizer(Extracted, header, Cookie, url):
    if 'TBS' in Extracted.split('"pageName":"')[1].split('"')[0]:
        data = TBS(Extracted, Cookie, url)
    else:
        data = solution(Extracted, header)
    return(data)


def likeIt(link):
    selec_cookie = random.choice(chegg_cookies)
    header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': "application/x-www-form-urlencoded; charset = UTF-8",
        'cookie': selec_cookie,
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        "sec-ch-ua-platform": "Windows",
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Mobile Safari/537.36'
    }
    content = requests.get(link, headers=header).text
    askerId = content.split('data-askerId="')[1].split('"')[0]
    entityId = content.split('data-answerId="')[1].split('"')[0]
    header['accept'] = 'application/json, text/javascript, */*q = 0.01'
    answerDate = content.split(
        'data-ansCreateDate="')[1].split('"')[0].replace(':', '%3A')
    questionId = content.split('data-qid="')[1].split('"')[0]
    token = content.split('"token":"')[1].split('"')[0]
    query = 'askerId={}&entityType=ANSWER&entityId={}&reviewType=LIKE_DISLIKE&reviewValue=0&answerCreatedDate={}&token={}&questionId={}'.format(
            askerId, entityId, answerDate, token, questionId)
    try:
        liked = requests.post('https://www.chegg.com/study/_ajax/contentfeedback/savereview',
                              headers=header, data=query).json()['httpCode']
        return liked
    except:
        return 400


@app.route("/")
def new():
    return "This is the main Page"


@app.route("/v1/unlock", methods=['GET', 'POST'])
def chegg_v1():
    data = request.get_json()
    Cookie, header, Responce = ContentGrabber(data["url"])
    Extracted = Responce.text
    solution = SolutionFinalizer(Extracted, header, Cookie, data["url"])
    return solution


@app.route("/check")
def check():
    return render_template("new911.html")


@app.route("/v1/grab-sol", methods=['GET', 'POST'])
def grabSOl():
    data = request.get_json()
    header = {
        'authority': 'atc-edge.studybreakmedia.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'script',
        'referer': f'{data["url"]}',
        'cookie': f"{random.choice(chegg_cookies)}",
        'accept-language': 'en-US,en;q=0.9',
    }
    resp = requests.get(data['url'], headers=header)
    text_Resp = resp.text
    open("response.html", "w", encoding="utf-8").write(text_Resp)
    if int(resp.status_code) == 403:
        return jsonify(code="301", text="Server is down, Try again later.")
    elif '"answeredStatus":"None"' in text_Resp:
        return jsonify(code="301", text="This question hasn't been solved yet")
    elif 'TBS' in text_Resp.split('"pageName":"')[1].split('"')[0]:
        typeOfSol = "textbook"
    else:
        typeOfSol = "qa"
    try:
        uuid = text_Resp.split('"pageNameDetailed":"')[1].split('"')[0]
    except:
        try:
            uuid = text_Resp.split('"questionUuid":"')[1].split('"')[0]
        except:
            try:
                uuid = text_Resp.split('"uuid":"')[1].split('"')[0]
            except:
                uuid = text_Resp.split('"questionId":')[1].split(',')[0]
    return jsonify(code="200", uuid=uuid, type=typeOfSol)


@app.route("/v1/upvote", methods=['GET', 'POST'])
def upvote():
    data = request.get_json()
    state = data["state"]
    if state == 0 or state == "0":
        ups = int(data["do"])
        done = []
        count = 0
        crisp = 0
        while count < int(ups):
            while True:
                cookie = random.choice(chegg_cookies)
                if cookie not in done:
                    break
            # try:
            response = newlikeIt(data["url"], cookie)
            if response[0] == 403:
                if crisp == 4:
                    break
                else:
                    crisp += 1
            elif response[0] == 200:
                count += 1
                crisp = 0
                done.append(cookie)
            else:
                print("error")
            # except:
            # 	pass
            time.sleep(random.randint(2, 5))
        return jsonify(code="100", added=count)
    else:
        resp = grb_det(data["url"])
    if resp["code"] == "303":
        return resp
    return jsonify(data=resp, code="1")


app.run(host="0.0.0.0", port=0000)
