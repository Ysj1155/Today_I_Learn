# *args"와 **kwargs    
## arguments
*args는 가변인자를 위한 변수. arg는 변수명이기 때문에 어떤 변수명을 입력해도 상관은 없지만 앞에 *는 붙여야한다.  
*args는 개수 상관 없이 모든 입력 인수를 튜플로 변환해주는 변수이다.  
```python  
def add(*args):
    result = 0
    for i in args:
        result += i
    print(result)
    
add(1, 10, 1302)
add(1, 2, 3, 19)
add(5)
```
출력값
```
1313
25
5  
```
위 코드는 args 안에 저장된 값을 result에 모두 더하는 함수이다.

## keyword arguments
**kwargs는 모든 key=value 형태의 입력 인수들을 딕셔너리로 변환해주는 변수이다.   
arg와는 달리 파라미터 명을 같이 보낼 수 있다. 
```python
def print_kwargs(**kwargs):
    print(f"type(kwargs) = {type(kwargs)}")
    for key, value in kwargs.items():
    print(f"{key} : {value}")
```
실행 결과
```
type(kwargs) = <class 'dict'>
first : Hello
second : World
```

하나의 def 안에 *args와 **kwargs를 동시에 쓸 수 있다.  
함수 선언 시 *args와 **kwargs를 같이 사용하는 경우, *args가 무조건 **kwargs보다 앞에 선언되어야 한다.  
그렇지 않으면 SyntaxError.  
함수 선언 시 non-default parameter (default 값이 없는 파라미터)가 default parameter (default 값이 있는 파라미터)보다 앞에 와야 하는 것과 동일하게 생각하면 된다.
```python
def print_args(*args, **kwargs):
    print(f"type(args) = {type(args)}")
    for arg in args:
        print(arg)
    print(f"type(kwargs) = {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key} : {value}")
```
실행 결과
```
type(args) = <class 'tuple'>
Hello
World
type(kwargs) = <class 'dict'>
first : Nice
second : Weather
```
