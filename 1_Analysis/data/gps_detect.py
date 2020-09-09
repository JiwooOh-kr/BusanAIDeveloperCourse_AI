# 카카오 api를 이용하여 키워드를 넣으면 gps를 획득하는 모듈
# 확장 -> gps 넣어서 주소 획득 or 주소 넣어서 gps 획득 or ...

import urllib
import urllib.request
import json

TARGET_URL = "https://dapi.kakao.com/v2/local/search/keyword.json"
KAKAO_API = 'KakaoAK ea6ae64692fc94aebea7ba2b61f3816a'

def getGpsByKeyword( keyword = "서울종로경찰서" ) :
  request = urllib.request.Request( f"{ TARGET_URL }?query={ urllib.parse.quote(keyword) }" )
  request.add_header('Authorization', KAKAO_API)
  response = urllib.request.urlopen(request)
  if response.getcode() == 200 :
    tmp = json.load(response)
    addr,lng, lat = tmp['documents'][0]['address_name'], tmp['documents'][0]['x'], tmp['documents'][0]['y']
  else :
    # 통신 실패하면 세팅하는 기본값
    addr,lng, lat = ('', 0, 0)
  return addr, lng, lat
