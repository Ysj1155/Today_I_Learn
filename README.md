# Today_I_Learn
# Today_I_Learn
=====================
하루 배운 내용 정리하기

# 1. 2/6 할 일과 한 일
* [x] git이랑 익숙해지기  
터미널에 git status 입력해서 commit할 변경 상태 확인.  
commit전에 git add . 로 모든 변경사항 추가  
git commit -m test.html로 github에 push  
깃허브에서 작성했던 위 내용을 파이참 내부에서 git pull로 업데이트 해보기.  

# 2. 2/7 할 일과 한일
* [ ] 내부 페이지 검색 기능을 위해서 무얼 알아야 되나 파악하기  
Buildblock Property, Commercial Property 페이지에서 제목 옆에 콤보상자처럼
검색 상자를 만들 구상중. 해당 페이지는 buildblock_property_list.html파일.  
* [ ] Homework 검색 페이지 만들어서 결과 보는 페이지 제작하기. 매물들 리스트에서 밑에 검색 박스에 검색 
버튼하고 해서 조건 안되면 안띄우고 조건 맞으면 매물 띄우는 그런 페이지
* [x] 파이참에서 터미널 입력으로 git push하기. 
여기서 git commit -m "파일 이름"으로 커밋
* [x] 3000포트에 매니저 버튼 생기게 권한 부여하기  
<img src="..%2F..%2FDesktop%2Fevidence.png" width="50" height="100"/>
위 사진은 로컬에 저장된 사진인데 안보인다. 이문장은 pull 실험용 문장.
PM에 대한 권한 부여 문제를 해결 필요. admin 페이지 안에서 권한 부여하면 다음 
화면이 나오는게 맞다고 하시니 내일까지 도전하는거로. 

공부한 내용
---------
>local host 3000포트: 프론트쪽. CSR(Client Side Rendering).  
클라의 웹 브라우저에서 랜더링 일어남. 서버는 클라에 최소한의 HTML을 보낸다. 자바스크립트
파일이 로드되며 컨텐츠가 동적으로 랜더링. 초기 로딩이 빠르진 않지만 콘텐츠를 제공하는데 
효과적. 원하는 내용만 업데이트가 가능하기 때문에 프론트 쪽에서 유용하게 쓰는건가

>local host 8000포트: 백엔드쪽. SSR(Server Side Rendering).  
서버에서 초기 HTML 생성해서 클라에 전송.
클라의 요청 마다 서버에서 데이터 가져와서 완성된 HTML 생성하고 이를 클라에 응답.
초기 페이지 로드할 때 서버에서 전부 랜더링 된 HTML을 받아 화면에 띄워 
유저에게 빠른 제공 가능. 3000 포트와 8000포트 사이에서 API통해 통신.  

# 3. 2/8 한 일과 할 일 
* [ ] Homework 검색 페이지 만들어서 결과 보는 페이지 제작하기. 매물들 리스트에서 밑에 검색 박스에 검색 
버튼하고 해서 조건 안되면 안띄우고 조건 맞으면 매물 띄우는 그런 페이지.  
 Django Search Tutorial 진행중. 작업 끝나면 빌드블록 property 활용해서 숙제 진행해볼 예정 
한 페이지 내 제목 밑에 리스트가 나열되고 그 밑에는 검색박스와 검색버튼. 검색박스에 일부를 입력해 버튼을 누르면 
같은 페이지에서 필터링된 결과가 검색박스 밑에 뜨는 페이지. 만약 검색결과가 없으면 없다고 알려주는 기능으로. 
더 나아가 빌드블럭 데이터를 가져와서 같은 방법으로 페이지 만들기까지.

* [x] admin 페이지 매니저 권한 습득, 진입 해보기.   
 정답은 profile managers에서 권한 부여하는 것이다. 준경님 도움 받아 권한 받음. buildblock.io/asibi로 
admin 페이지로 진입. 3000포트의 매니저 block의 부동산 상품 페이지에 접근. 내가 검색 박스를 만들 매니저 솔루션의 
매물 페이지 확인. 

# 4. 2/13 한 일과 할 일
* [ ] 이전 페이지 만드는 작업 이어서 진행중. admin 페이지에 저장된 데이터들을 home화면에 전부 보이는 방법 찾는중. 
일단 틀린 정보 입력했을 때 No Data 띄우기까지 함. null 값하고 space만 입력했을때에도 노데이터 띄우게 수정 필요. 
홈페이지 호스트주소/home 하면 화면이 안띄워지기 시작하는데 이슈 보완 필요하다 생각. home 화면에 city 리스트 띄우는거만 되면 
과제는 완료. 일단 double space는 no data가 정상적으로 출력된다. null값을 입력 했을 때 
전체 리스트가 나오는건 어쩔 수 없는건가 싶다. 
* [x] buildblock github의 최근 내용 pull. 준경님 3개월 매물 관련 pr이 업데이트 안된 이전 버전으로 pull되어 
최신화 방법 찾는중. 우선 git pull "주소"로 pull 진행함.

# 5. 2/14 
*[ ] administrator Ordering 작업 스타트. Buildblock Property의 매물 검색을 위한 Search box 만들어서 검색 
도와주는게 이번 업무의 목적. 페이지도 24page로 많아 매물 찾는게 힘들다라는게 불편 포인트. 추가로 type별로 6개 분류가 있는데
Tread Class에서 Type을 콤보상자로 분류되게 하는게 second 목표. Q함수를 이용해 필터 작업하는게 키포인트로 보인다.    
buildblock_property_list.html에서 <t body>안의 buildblock_property.property_basic.full_address가 
주소의 객체인거로 파악. 이 객체를 Q함수로 필터링하려면 무슨 지식이 필요할까  

장고 ORM(Object Relational Mapper). 객체 지향적인 방법을 사용하여 데이터베이스의 데이터를 쉽게 조작. 조건 키워드에서
1. model.objects.filter(name__contains='Welcome')
2. model.objects.filter(name__icontains='Welcome')
에서 1번은 문자 검색이 가능하고 2번은 대소문자를 구분하지 않는다고 한다.  

Get은 한개의 데이터만 추출하는 함수고 Filter는 여러개의 데이터를 추출할 때 쓰는 함수다. property_basic.full_address
데이터만 필요하니까 get함수로 이 데이터를 추출해서 보여주는 함수 만들면 되지 않을까. 지금 고민하는건 필터 함수를 어느 html파일에
넣어야 원하는 대로 작동할까

# 6. 2/15
"*args"와 "**kwargs"  
arguments와 keyword arguments의 약어. *args는 개수와 상관 없이 모든 입력 인수를 튜플로 변환해주는 변수. 
**kwargs는 모든 key=value 형태의 입력인수를 딕셔너리로 변환해주는 변수.   

"'<"form">"태그의 enctype 속성은 form data가 서버로 제출될 때 해당 데이터가 인코딩되는 방법 명시하는 기능.
<"form>" 요소의 method 속성값이 “post”인 경우에만 사용.  

html에서 csrf_token은 CSRF(Cross Site Request Forgery,user가 자신의 의지와 무관하게 공격자가 의도한 행동을 특정
웹사이트에 요청하게 하는 공격; 이미 사용자가 접속한 상황에서 요청값을 조작하여 사용자가 원하지 않는 action을 보내 웹 어플리케이션을 악용)
를 방지하기 위해 django에서 제공하는 기능. 

# 7. 2/20
깃허브 pr 올리기  
git add로 바꿀 파일 안전하게 하나씩 지정해서 올리기 pre-commit run으로 다른 사람들이랑 쓰는 
문법같은거 싱크 맞는지 확인하고 git branch로 각 올릴 pr마다 branch를 sjYoon/하는 일 
이런 식으로 새로 파서 이 브랜치를 빌드블록으로 push하기

# 8. 3/2
리스트(list)  
요소를 삭제하거나 변경 가능. mutable(가변성), iterable(순차적)  
list + list 형식으로 서로 다른 리스트 붙임 가능.   
하나의 리스트 안에 서로 다른 type의 요소들을 담을 수 있다. 
>l = [], l = list()                   //리스트 선언  
list(seq)                             // 리스트로 변환  
l.append(1)                           // list에 값 1을 요소로 추가한다.  
l.insert(2, 'data')                   // list의 두 번째 요소에 'data'를 삽입한다.  
del l[index]                          // index 기반 삭제  
l.remove(삭제할값)                      // value 기반 삭제  
l.pop()                               // list의 tail 삭제 및 반환  
l.pop(0)                              // list의 head 삭제 및 반환  
l.extend(new_list), l+= new_list      // list l과 new_list를 병합한다.   
b = l.copy(), b = list(l), b = l[:]   // list l의 복사값을 b에 대입   
l.index('data')                       // list 요소 중 'data'의 인덱스 반환  
'data' in l                           // list에 'data' 요소가 있는지 True, False 반환  
l.count('data')                       // 'data' 개수 확인  
", ".join(l)                          // ,를 기준으로 list를 문자열로 만든다.  
sorted(l)                             // 정렬된 복사본을 반환  
l.sort()                              // list 자체를 정렬한다.  
len(l)                                // list 개수 세기  
max(l)                                // 요소 중 최대값  
min(l)                                // 요소 중 최소값

튜플(Tuple)  
요소를 삭제하거나 변경 불가능. immutable(불변성), iterable(순차적)  
tuple + tuple 형식으로 서로 다른 튜플 붙이기 가능(new_tuple = t1 + t2)  
tuple은 append(), remove() 안됨. 처음 선언시 자료구조를 선언(t1 = (1, 2))  
서로 다른 타입의 요소를 하나의 tuple에 담을 수 있다. (t1 = ('a', 1, 3))
>t = (seq)        // 튜플로 변환  
t.count           // 요소 개수  
t.index(2)        // 요소 위치 index  
len.(t)           // 튜플 길이  
max.(t)           // 요소 중 최대값  
min.(t)           // 요소 중 최소값  
 
셋(Set)  
요소의 중복이 불가능한 내장 모듈 collection 자료형.  
mutable, not iterable.  
중복 제거, 교집합, 합집합등 수학적 계산 가능.  
add(), update(), remove() 매서드 사용 가능.  
>s1 = {1, 2, 3, 4, 5}             // s1셋 선언  
s2 = {3, 5, 7, 9}                // s2셋 선언  
s = set([1,2,2,3,3,3,4,4,4,4]) // 셋으로 변환  
s.add(5)                       // 요소 추가  
s.update([6,7,8])              // 여러개 요소 추가  
s.remove(8)                    // 요소 삭제  
s1|s2                          // s1 s2 합집합  
s1&s2                          // s1 s2 교집합  
s1-s2                          // s1 s2 차집합  
s1^s2                          // s1 s2 대칭 차집합  

딕셔너리(Dictionary)  
중복 불가능한 collection 자료형.  
mutable(가변성)  
key-value 구조. dic={'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}  
key 중복 안됨.  
>d = dict()              // 딕셔너리 선언  
d.keys()                // 딕셔너리의 키 목록  
d.values()              // 딕셔너리의 값 목록  
d.items()               // 딕셔너리의 key-value 튜플 목록  
d.clear()               // 딕셔너리의 모든 요소 삭제  
d.copy()                // 딕셔너리 복사  
d.fromkeys()            // seq, value 셋으로 딕셔너리 생성  
d.get(key, default=None) // 해당 키의 저장된 값 확인  
d.setdefault(key, default-None) // 해당 키의 저장된 값 확인(만약 값이 없으면 None)  
d.update(d2)            // 딕셔너리에 'd2'라는 딕셔러니를 추가  
len(d)                  // 딕셔너리 길이  
str(d)                  // 딕셔너리를 문자열로 변환  
