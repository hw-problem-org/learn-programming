package com.example.grpcperform

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import io.grpc.ManagedChannel
import io.grpc.ManagedChannelBuilder
import java.util.*

class MainActivity : AppCompatActivity() {
    private lateinit var channel:ManagedChannel
    private lateinit var stub: TestServiceGrpc.TestServiceBlockingStub

    private var timeOffsetMill:Long = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        channel = ManagedChannelBuilder.forAddress("192.168.43.21",50051).usePlaintext().build()
        stub = TestServiceGrpc.newBlockingStub(channel)
        val button = findViewById<Button>(R.id.button)
        button.setOnClickListener( object : View.OnClickListener{
            override fun onClick(v: View?) {
                onButtonClick()
            }
        })
    }

    fun onButtonClick(){
        val timeStamp = System.currentTimeMillis() - timeOffsetMill
        val request = TimeStamp.newBuilder().setMilliseconds(timeStamp).build()
        val time_s = System.currentTimeMillis()
        stub.ping(request)
        val time_e = System.currentTimeMillis()
        Log.d("Perform", "Latency: ${time_e - time_s}")
    }

}
