package com.example.orient

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ImageView

class LandscapeActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_landscape)
        val image_view = findViewById<ImageView>(R.id.imageView)
        image_view.setImageResource(R.drawable.stick_man)
    }
}