# 🔥 취준 지옥 탈출 🔥

<table>
  <tr>
    <td>진행 기간</td>
    <td>2024년 8월 28일 ~ </td>
  </tr>
  <tr>
    <td>플랫폼</td>
    <td>프로그래머스</td>
  </tr>
   <tr>
    <td>장소</td>
    <td>온라인, 재정정보원</td>
  </tr>
  <tr>
    <td>언어</td>
    <td>Java, Python, C++</td>
  </tr>
</table>

---

## **📅 일정표 (09.02 ~ 매주 5문제)**
| |1|2|3|4|5|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1주차(09.02~09.08)|[타겟 넘버(DFS/BFS)](https://school.programmers.co.kr/learn/courses/30/lessons/43165)|[올바른 괄호(스택/큐)](https://school.programmers.co.kr/learn/courses/30/lessons/12909)|[카펫(완전탐색)](https://school.programmers.co.kr/learn/courses/30/lessons/42842)|[문자열 압축(문자열)](https://school.programmers.co.kr/learn/courses/30/lessons/60057)|[가장 큰 수(정렬)](https://school.programmers.co.kr/learn/courses/30/lessons/42746)|
|2주차(09.09~09.15)|[수식최대화(완전탐색)](https://school.programmers.co.kr/learn/courses/30/lessons/67257)|[전력망을 둘로 나누기(DFS/BFS)](https://school.programmers.co.kr/learn/courses/30/lessons/86971)|[정수 삼각형(DP)](https://school.programmers.co.kr/learn/courses/30/lessons/43105)|[삼각 달팽이(구현)](https://school.programmers.co.kr/learn/courses/30/lessons/68645)|[조이스틱(그리디)](https://school.programmers.co.kr/learn/courses/30/lessons/42860)|
|3주차(09.19~09.22)|[배열 돌리기1(구현)](https://www.acmicpc.net/problem/16926)|[ABCDE(DFS/BFS)](https://www.acmicpc.net/problem/13023)|[가장 긴 증가하는 부분 수열(DP)](https://www.acmicpc.net/problem/11053)|[빗물(구현)](https://www.acmicpc.net/problem/14719)|[숨바꼭질(DFS/BFS)](https://www.acmicpc.net/problem/13549)|

---

## ✔️ 문제 선정
  - 개수 : 주 5개
  - 알고리즘 유형 : 그래프탐색, 완전탐색, 문자열, DP, 구현, 해시 등
  - 난이도 : 프로그래머스 lv2로 시작하여 lv3로 점진적 변화  
   
## ✔️ 풀이 방식 
    - 월요일에 5문제를 공개하고, 다가오는 일요일까지 풀이 진행하시면 됩니다. (개인 일정에 따라 유동적으로 진행하시면 됩니다)
    
    - 코드리뷰 진행x, 필요에 따라 다른분의 코드를 보고 질의응답을 진행하시면 됩니다

## ✔️ 벌금제
  - 해당 주차 문제 5개 풀이를 못할 경우, 벌금 3만원
  - 어려워서 못푸는 문제는 상세 코멘트 必

        ex)  
        해당 문제를 보자마자 그리디가 떠올랐는데, 해결이 되지 않았습니다. 
        이후 DP 접근 방식을 떠올리긴했지만, 접근 로직이 명확히 떠오르지 않았습니다. 
        점화식에 대한 공부가 더 필요하다고 느꼈습니다. 
        n번 라인에서 ~~로직을 떠올리지 못했습니다

        def solution(N, number):
        S = [0, {N}]

        for i in range(2, 9):
          case_set = {int(str(N)*i)}
          for j in range(1, i//2+1):  # S[i_half] S[1]

---

## 👶 폴더 구조

    - N주차(mm.dd~mm.dd)
      - 본인 이름 폴더 (ex. kimyongsang) 
        - 문제 풀이 파일 (ex. 하노이탑.py )      
    - readme.md
