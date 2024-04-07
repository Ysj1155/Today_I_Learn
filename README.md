# Today_I_Learn
git

[git-strategy](git/git-branch-strategy)


python

[리스트, 셋, 튜플, 딕셔너리](python/List,Set,Tuple,Dictionary.md)



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



