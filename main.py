# -*- coding: utf-8 -*-
import re
from ko_pron import romanise

class Rhyme:
    start_index = 0
    end_index = 0

    def __init__(self, start_index, end_index):
        self.start_index = start_index
        self.end_index = end_index

def isHangul(text):
    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text))
    return hanCount > 0

lyrics = """아직 기억하네, 1988년
MJ의 Moon Walker
어떤 의미에선 그때 처음 음악에 눈을 떴어
사촌들과 친척들 앞에서 그 춤을 췄어
그리고 어린 게 피아노를 곧잘 쳐
어머니 애창곡으로 악보를 골라서
연주할 때면 어머니의 얼굴에서
미소를 볼 수 있었고 난 우쭐했어
그러니까 내 가족이 내 최초의 관객
실내화, 크레파스, 스케치북, 가방, 책
드래곤볼. 다른 애들과 똑같애
다른 점이라면 창의력 뛰어난 학생
Corleone에서 Tony Montana, Carlito로
박하사탕에서 역도산, 실미도로
노원구에서 바로 강남으로
그리고 내 유년기는 바로 다음 장으로
New Kids on the Block, 스트리트 파이터 2
벌써 담배 맛을 아는 형들이 알려준
돈이 없어도 조던 가질 수 있는 법
혹시 들켜도 어른들 속이고 튀는 법
But I never was a 양아 type. Rather 민감한 type
그런 내게 다가온 중2 때 장기자랑 night
누군가의 땜빵으로 내가 불렀던 노래
라디오에서 들은 김현철의 "동네"
내 걱정과는 달리 천여명이 환호해
It was so spiritual, I thought it was 교회
다음날 아침조회부터
여자애들이 내게 말 걸었어 like "Hey what's up?"
각하에서 역사의 도마 위로
운동권에서 정권의 노른자위로
Pearl Jam에서 The Fugees로
I was changing, but no one could see it though
TR-808에서 Motif로
스쿨 밴드에서 한국 힙합 엘리트로
만 17세, 학교를 자퇴할 때쯤 힙합 클럽에 가
공연들을 보며 들은 생각, '고작 저게 다?'
무열정, 무질서한 낱말들의 나열
This art form, someone's gotta take it to higher ground
So "How High School", 내 첫 가사
그리고 Show N Prove, 우린 영향을 주고 받아
한국말 랩의 새로운 세대의 탄생
시대가 완전히 바뀌어 버렸지. 한땐
"학교 종교 육교" 거리던 이들이
차츰 머릴 쓰기 시작해. 혁명은 이미
돌이킬 수 없는 단계로 왔어
그 과정의 나침반이자 교과서
The one and only VJ, and now I'm back again
물론 이번에도 변화의 핵, again"""

pron_list = []

for text in lyrics:
    pron = ""

    if isHangul(text): #한글이면
        pron = romanise(text, "rr")
    else: #이외의 글자이면
        pron = None

    pron_list.append(pron)

pron_list_len = len(pron_list)
search_limit = 25

for i in range(pron_list_len):
    now_search_limit = i + search_limit

    if now_search_limit > (pron_list_len - 1): #검색 limit 값이 리스트 끝을 넘어간다면
        now_search_limit = (pron_list_len - 1)

    for j in range(i + 1, now_search_limit + 1): #검색 중...
        if pron_list[i]
