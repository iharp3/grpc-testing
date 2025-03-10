# gRPC Testing

## Running the project
To run the project, run `dbnode_server.py` on each of your database nodes. They'll accept requests from the main node, which you'll run `db_client.py` on.

## Modifying the project

If you ever change the .proto files, you need to use gRPC to update some of the .py files. 

Run `cd src` and `python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/testing.proto` in order to do so. This calls gRPC to regenerate the communication files (the .py files with `pb2` in them).