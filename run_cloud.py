#!/usr/bin/env python3
"""Render/Cloud 환경 전용 진입점
- 환경변수 PORT를 읽어 바인딩
- 0.0.0.0으로 외부 접속 허용
- 브라우저 자동 실행 비활성화
"""
import os
import sys

port = os.environ.get("PORT", "8000")
try:
    port = int(port)
except ValueError:
    port = 8000

# run.py의 main 실행 함수를 인자와 함께 호출
sys.argv = ["run.py", "--host", "0.0.0.0", "--port", str(port), "--no-browser"]

import run
run.main()
