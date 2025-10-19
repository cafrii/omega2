# node.js 환경 설정

## 목적
- javascript, typescript 를 사용한 문제 해결

## 선택 옵션 검토
- 옵션
  - 1. 전역 설치
  - 2. npx
  - 3. 프로젝트 생성 후 로컬 설치
- boj 문제 풀이의 경우 추가 패키지를 필요로 하지 않을 가능성이 높음.
- 하지만 그냥 관례대로 프로젝트를 생성해서 진행하기로 함.

## 절차

- 현재 환경 정보 확인
```
$ node -v
v24.8.0

$ npm -v         # npm 버전 확인
11.6.0

$ npx -v         # npx 호출 가능 확인 (npm 에 포함되어 있음)
11.6.0

$ nvm -v         # nvm 동작 확인.
0.39.1

$ which node     # ~/.nvm/... 를 가리키면 nvm 경로 사용 중
~/.nvm/versions/node/v24.8.0/bin/node
```

- node 실행 전용 폴더 생성
```
mkdir node && cd node
```

- 초기화
```
npm init -y

# package.json 생성됨.
```

- tsc 설치
```
npm install --save-dev typescript
```

- 문제 풀이를 위한 필수 패키지들
```
npm i -D @types/node

npm i -D ts-node

```

- tsconfig 생성
```
npx tsc --init
```

- tsconfig.json 수정. types 에 "node" 추가.
```
vi tsconfig.json
...
    "types": ["node"],

```

- 실행하기
```
npx ts-node <file>.ts
```

## 문제 해결
- git clone 후 처음 설치
```
npm install
```

