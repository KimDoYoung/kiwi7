---
description: 로그파일을  tail 로 읽어서 오류를 확인하고 수정한다.
allowed-tools: Read, Write, Edit, Grep, Glob
argument-hint: [오류 수정]
---

# 개요

로그파일을 tail 도구를 이용해서 읽은 후 오류를 확인하고 오류의 수정방법을 사용자에게 알린다. 그런 후 사용자가 허락하면 수정한다.

## 작업 흐름

### 1. 로그 파일의 위치 확인

1. **개발 machine확인**: os와 hostname을 확인한다.
   1. os가 linux이고 hostname os이면 로그파일은 `/home/kdy987/data/kiwi7/logs/kiwi7.log` 이다.
   2. os가 window이고 hostname `KDY-3560` 이면 `c:\tmp\kiwi7\logs\kiwi7.log` 이다
   3. 로그파일을 찾지 못했을 경우 사용자에게 알리고 **작업을 중단** 한다.

2. **오류확인**: tail 로 오류를 확인한다.

3. **수정방향제시** : 사용자에게 수정방향을 제시하고 사용자의 허락을 요구한다.
   1. 주의 : 무작성 수정하지 않는다.
