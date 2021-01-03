import requests
import json
import pandas as pd

"""
使用 requests 库抓取知乎任意一个话题

--话题：听完国家主席习近平发表的 2021 年新年贺词，你有怎样的感触？对于自己的 2021 年有什么期待？

排名前 15 条的答案内容 
(如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件。
"""

def html_data(myurl):
    header = {'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
                }
    try:
        response = requests.get(myurl, headers=header)
        response.raise_for_status()
        return response.text   
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error!")
        
def parse_data(html):
    json_data = json.loads(html)['data']
    comments = []
    try:
            for i in json_data:
                comment = []
                comment.append(i['author']['name'])    # 姓名
                comment.append(i['excerpt'])      # 回答内容
                comments.append(comment)
                # print(comment)
                return comments        
    except Exception as e:
            print(comment)
            print(e)
def save_data(comments):
    filename = "spider.txt" 
    dataframe = pd.DataFrame(comments) 
    dataframe.to_csv(filename, mode='a', index=False, sep=':', header=False)
    # exit(0)
    
def main():   
    myurl = "https://www.zhihu.com/api/v4/questions/437329650/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=30&platform=desktop&sort_by=default"  
    html = html_data(myurl)
    totals = json.loads(html)['paging']['totals']  
    print(totals)
    print('---'*10)  
    page = 0   
    while(page < totals):
        myurl = "https://www.zhihu.com/api/v4/questions/437329650/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset="+ str(page) +"&platform=desktop&sort_by=default"
        html = html_data(myurl)
        comments = parse_data(html)
        save_data(comments)      
        print(page)
        page += 5   
if __name__ == '__main__':
    main()
    print("完成！")