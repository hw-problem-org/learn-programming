package com.example.orient

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.ImageView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val image_view = findViewById<ImageView>(R.id.imageView)
        image_view.setImageResource(R.drawable.stick_man)

        var button = findViewById<Button>(R.id.button)
        button.setOnClickListener( object : View.OnClickListener{
            override fun onClick(v: View?) {
                Log.d("Button", "Click!")
                val intent = Intent(this@MainActivity, LandscapeActivity::class.java)
                startActivity(intent)
            }
        })
    }
}