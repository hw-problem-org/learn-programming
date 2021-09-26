package com.example.clickme

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        var button = findViewById<Button>(R.id.button)
        button.setOnClickListener( object : View.OnClickListener{
            override fun onClick(v: View?) {
                Log.d("Button", "Click!")
            }
        })

    }
}