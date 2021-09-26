#!/bin/bash
python3 -m grpc_tools.protoc -I../grpc-perform-android/app/src/main/proto --python_out=. --grpc_python_out=. perform.proto
