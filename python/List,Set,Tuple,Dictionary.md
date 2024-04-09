# 리스트(List)와 튜플(Tuple), 셋(Set)과 딕셔너리(Dictionary)

## 리스트(list)  
요소를 삭제하거나 변경 가능. mutable(가변성), iterable(순차적)  
list + list 형식으로 서로 다른 리스트 붙임 가능.   
하나의 리스트 안에 문자형, 실수, 정수 등 서로 다른 type의 요소들을 담을 수 있다.  
`l = [10, 'python', True]`
> l = [], l = list()                   //리스트 선언  
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

## 튜플(Tuple)  
요소를 삭제하거나 변경 불가능. immutable(불변성), iterable(순차적). 읽기 전용 리스트.    
tuple + tuple 형식으로 서로 다른 튜플 붙이기 가능(new_tuple = t1 + t2)  
tuple은 append(), remove() 안됨. 처음 선언시 자료구조를 선언(t1 = (1, 2))  
서로 다른 타입의 요소를 하나의 tuple에 담을 수 있다. (t1 = ('a', 1, 3))
튜플은 리스트와는 다르게 내용을 변경할 수 없기 때문에 append와 같은 메서드는 못 쓰고 
요소의 정보를 조회하는 메서드만 사용 가능하다.  
`t = (10, 20, 30)`  
>t = (seq)        // 튜플로 변환  
t.count           // 요소 개수  
t.index(2)        // 요소 위치 index  
len.(t)           // 튜플 길이  
max.(t)           // 요소 중 최대값  
min.(t)           // 요소 중 최소값

리스트와 튜플과 같은 시퀀스 자료형(순서가 있는 자료형, iterable)은 슬라이스가 가능.  
> a = [10, 20, 30, 40, 50, 60]  
> print(a[0:3])     //[10, 20, 30]  
> print(a[1:3])     //[20, 30]  
> print(a[0:5:2])   //[10, 30, 50]  
> print(a[-1])      //60  
> print(a[5:0:-1])  //[60, 50, 40, 30, 20]  
> print(a[::])      //[10, 20, 30, 40, 50, 60]  
  
## 셋(Set)  
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

##  딕셔너리(Dictionary)  
중복 불가능한 collection 자료형.  
mutable(가변성)  
key-value 구조.   
`dic={'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}`  
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
