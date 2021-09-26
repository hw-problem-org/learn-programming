package com.example.imucam

import android.annotation.SuppressLint
import android.graphics.*
import android.graphics.ImageFormat.NV21
import android.media.Image
import android.util.Log
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import androidx.camera.core.CameraSelector
import androidx.camera.core.ImageAnalysis
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.core.content.ContextCompat
import androidx.lifecycle.LifecycleOwner
import java.io.ByteArrayOutputStream
import java.nio.ByteBuffer
import java.util.concurrent.Executors

@SuppressLint("UnsafeOptInUsageError")
class Camera(activity: AppCompatActivity) {
    private val cameraProviderFuture = ProcessCameraProvider.getInstance(activity)
    init {
        cameraProviderFuture.addListener(Runnable {
            val imageAnalysis = ImageAnalysis.Builder()
                    .setBackpressureStrategy(ImageAnalysis.STRATEGY_BLOCK_PRODUCER)
                    .build()
            val cameraProvider = cameraProviderFuture.get()
            val cameraSelector = CameraSelector.Builder()
                    .requireLensFacing(CameraSelector.LENS_FACING_FRONT)
                    .build()
            val executor = Executors.newSingleThreadExecutor()
            imageAnalysis.setAnalyzer(executor, ImageAnalysis.Analyzer { image ->
                val rotationDegrees = image.imageInfo.rotationDegrees
                Log.d("aditya", "$rotationDegrees")
                var jpegImage: ByteArray? = image.image?.let { toJpegImage(it, 70) }
                if (jpegImage != null) {
                    val bitmap = BitmapFactory.decodeByteArray(jpegImage, 0, jpegImage.size)

                    val matrix = Matrix()
                    matrix.postRotate(-90F)
                    val rotatedBitmap = Bitmap.createBitmap(bitmap, 0, 0, bitmap.width, bitmap.height, matrix, true)

                    activity.runOnUiThread{
                        val imageView = activity.findViewById<ImageView>(R.id.imageView)
                        imageView.setImageBitmap(rotatedBitmap)
                    }
                }
                image.close()
            })
            cameraProvider.bindToLifecycle(activity as LifecycleOwner, cameraSelector, imageAnalysis)
        }, ContextCompat.getMainExecutor(activity))
    }
}

fun toJpegImage(image: Image, imageQuality: Int): ByteArray? {
    val yuvImage = toYuvImage(image)
    val width = image.width
    val height = image.height

    // Convert to jpeg
    var jpegImage: ByteArray? = null
    ByteArrayOutputStream().use{ out ->
        yuvImage!!.compressToJpeg(Rect(0, 0, width, height), imageQuality, out)
        jpegImage = out.toByteArray()
    }
    return jpegImage
}

fun toYuvImage(image: Image): YuvImage? {
    val yBuffer: ByteBuffer = image.planes[0].buffer
    val uBuffer: ByteBuffer = image.planes[1].buffer
    val vBuffer: ByteBuffer = image.planes[2].buffer
    val ySize: Int = yBuffer.remaining()
    val uSize: Int = uBuffer.remaining()
    val vSize: Int = vBuffer.remaining()
    val nv21 = ByteArray(ySize + uSize + vSize)

    // U and V are swapped
    yBuffer.get(nv21, 0, ySize)
    vBuffer.get(nv21, ySize, vSize)
    uBuffer.get(nv21, ySize + vSize, uSize)
    val width: Int = image.getWidth()
    val height: Int = image.getHeight()
    return YuvImage(nv21, NV21, width, height,null)
}