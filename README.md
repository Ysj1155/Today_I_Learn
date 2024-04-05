# Today_I_Learn
git

[git-strategy](git/git-branch-strategy)


python

[리스트, 셋, 튜플, 딕셔너리](python/List,Set,Tuple,Dictionary)


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



