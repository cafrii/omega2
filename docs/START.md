

# 또 하나의 저장소를 시작합니다!

private 으로 관리중인 몇 개의 유사한 저장소들이 있지만.. 새로운 마음으로, 다시, 또, 한번 더 시작합니다.

이번에는 자동으로 관리해 주는 툴을 활용합니다.


# BackjunHub

URL: <https://github.com/BaekjoonHub/BaekjoonHub>

코딩 연습으로 많이들 사용하는 백준 온라인 문제풀이 (https://www.acmicpc.net/) 사이트와 연동됩니다. 작성한 문제풀이를 자동으로 github 에 올려주는 확장 프로그램입니다.

>
> 백준 허브는 LeetCode의 개인 풀이를 github에 자동 푸시해주는 LeetHub에서 영감을 받아 만든 프로젝트입니다. 백준, 프로그래머스, goormlevel를 통해 알고리즘 공부를 하시는 분들이 더욱 쉽게 코드를 저장하고 관리할 수 있게 하도록 만들었으며, 오픈소스 프로젝트로 여러분의 조언과 참여를 환영합니다.
>

## 설치

크롬 웹스토어, 백준허브 확장을 설치합니다.
https://chromewebstore.google.com/detail/%EB%B0%B1%EC%A4%80%ED%97%88%EB%B8%8Cbaekjoonhub/ccammcjdkpgjmcpijpahlehmapgmphmk

크롬 브라우저에서 연동할 github 본인 계정에 로그인 해 둡니다.

크롬 브라우저 address bar (URL 주소 입력 칸) 우측의 확장 아이콘 중 백준허브 아이콘을 클릭하여 팝업을 표시하고, "Authenticate with GitHub to use BaekjoonHub" 아래 [Authenticate] 버튼을 클릭합니다.

'Authorize Baekjoonhub' 페이지가 뜨면 내용을 확인하고 'Authorize ...' 를 눌러줍니다.

접근 가능한 정보가 약간 필요 이상으로 과하다 싶긴 한데..

> This application will be able to read and write all public and private repository data. This includes the following:
> - Code
> - Issues
> - Pull requests
> - Wikis
> - Settings
> - Webhooks and services
> - Deploy keys
> - Collaboration invites
>
> Note: In addition to repository related resources, the repo scope also grants access to manage organization attributes and organization-owned resources including projects, invitations, team memberships and webhooks. This scope also grants the ability to manage projects owned by users.
>

오픈소스로 개발중인 확장인데 그냥 믿고 진행합니다.

크롬에서 `Bae/<joonHub>` 제목의 연동 페이지가 표시됩니다. 이 omega2 저장소를 선택하고 'organize by platform' 을 선택합니다.

다음과 같은 메시지가 나오면 끝입니다.
```
Successfully linked cafrii/omega2 to BaekjoonHub. Start BOJ now!

Linked the wrong repo? Unlink.
```

## 동작 확인

실제로 잘 동작하는지 확인해 보기 위해, `Baekjoon Online Judge
` <https://www.acmicpc.net/> 에 접속하여 아주 간단한 문제를 하나 풀어보기로 합니다.


https://www.acmicpc.net/problem/9086

문제 풀이를 '제출' 하고, 결과 컬럼에 '맞았습니다' 표시까지 되었는데 화면에는 아무런 반응은 없었습니다. 백준허브 README 에서는 업로드가 진행되는 것이 보이던데...

그렇지만 시간이 지난 후 확인해 보니 이 저장소에 다음 파일이 자동 커밋/푸시 되었음이 확인됩니다.

- 백준/Bronze/9086. 문자열/
  - README.md
  - 문자열.py

문제 번호 뿐 아니라 문제 이름까지 표시해 주니 알아보기에는 편합니다.

참고로, 실패한 문제풀이는 따로 기록을 남겨주는지는 모르니, 실패 코드는 별도로 관리해야 할지도 모르겠습니다.


