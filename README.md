# Today_I_Learn
===============
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
* [ ] 파이참에서 터미널 입력으로 git amend하기. 
여기서 git commit -m ""말고 한번에 왼쪽 commit 버튼처럼 커밋하는 방법 찾기
* [ ] 3000포트에 매니저 버튼 생기게 권한 부여하기  
<img src="..%2F..%2FDesktop%2Fevidence.png" width="100" height="200"/>  
PM에 대한 권한 부여 문제를 해결 필요  

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
유저에게 빠른 제공 가능. 

