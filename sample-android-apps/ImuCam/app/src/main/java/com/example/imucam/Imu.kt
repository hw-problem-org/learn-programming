package com.example.imucam

import android.content.Context
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class Imu (private val activity: AppCompatActivity): SensorEventListener {
    private var sensorManager: SensorManager = activity.getSystemService(Context.SENSOR_SERVICE) as SensorManager

    lateinit var accelerometer : Sensor
    init {
        if (sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER) != null) {
            accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)
            accelerometer?.also { acceleration ->
                sensorManager.registerListener(this, acceleration, SensorManager.SENSOR_DELAY_NORMAL)
            }
        }
    }

    lateinit var gyroscope : Sensor
    init {
        if (sensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE) != null) {
            gyroscope = sensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE)
            gyroscope?.also { angularRate ->
                sensorManager.registerListener(this, angularRate, SensorManager.SENSOR_DELAY_NORMAL)
            }
        }
    }

    lateinit var magnetometer : Sensor
    init{
        if (sensorManager.getDefaultSensor(Sensor.TYPE_ROTATION_VECTOR) != null) {
            magnetometer = sensorManager.getDefaultSensor(Sensor.TYPE_ROTATION_VECTOR)
            magnetometer?.also { orientation ->
                sensorManager.registerListener(this, orientation, SensorManager.SENSOR_DELAY_NORMAL)
            }
        }
    }

    override fun onAccuracyChanged(sensor: Sensor, accuracy: Int) {
        //TODO
    }

    override fun onSensorChanged(event: SensorEvent) {
        if(event.sensor.type == Sensor.TYPE_ACCELEROMETER){
            val ax = event.values[0]
            val ay = event.values[1]
            val az = event.values[2]
            val textViewAccelerometer = activity.findViewById<TextView>(R.id.textViewAccelerometer)
            textViewAccelerometer.text = "ax: ${"%.2f".format(ax)}, ay: ${"%.2f".format(ay)}, az: ${"%.2f".format(az)}"
        }else if (event.sensor.type == Sensor.TYPE_GYROSCOPE){
            val wx = event.values[0]
            val wy = event.values[1]
            val wz = event.values[2]
            val textViewGyroscope = activity.findViewById<TextView>(R.id.textViewGyroscope)
            textViewGyroscope.text = "wx: ${"%.2f".format(wx)}, wy: ${"%.2f".format(wy)}, wz: ${"%.2f".format(wz)}"
        }else if (event.sensor.type == Sensor.TYPE_ROTATION_VECTOR){
            val x = event.values[0]
            val y = event.values[1]
            val z = event.values[2]
            val w = event.values[3]
            val textViewMagnetometer = activity.findViewById<TextView>(R.id.textViewMagnetometer)
            textViewMagnetometer.text = "x: ${"%.2f".format(x)}, y: ${"%.2f".format(y)}, z: ${"%.2f".format(z)}, w: ${"%.2f".format(w)}"
        }
    }
}