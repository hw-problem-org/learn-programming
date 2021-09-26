package com.example.grpchelloworld

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import io.grpc.ManagedChannelBuilder

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val channel = ManagedChannelBuilder.forAddress("192.168.43.21",50051).usePlaintext().build()
        val stub = GreeterGrpc.newBlockingStub(channel)
        val request = HelloRequest.newBuilder().setName("Aditya").build()
        val reply:HelloReply = stub.sayHello(request)
        Log.d("grpc_msg", reply.message)
    }
}