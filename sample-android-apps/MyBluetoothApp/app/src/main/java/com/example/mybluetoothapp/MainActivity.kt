package com.example.mybluetoothapp

import android.bluetooth.BluetoothAdapter
import android.bluetooth.BluetoothDevice
import android.bluetooth.BluetoothSocket
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.textfield.TextInputEditText
import java.io.IOException
import java.util.*

class MainActivity : AppCompatActivity() {
    lateinit var messageInputEditText:TextInputEditText
    lateinit var button:Button
    lateinit var statusView: TextView

    private lateinit var bluetoothHandler: BluetoothHandler

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        bluetoothHandler = BluetoothHandler()

        getUiResources()
        button.setOnClickListener(ButtonClickListner())
        statusView.text = "Not Connected!"

    }

    fun getUiResources(){
        messageInputEditText = findViewById<TextInputEditText>(R.id.message)
        button = findViewById<Button>(R.id.button)
        statusView = findViewById<TextView>(R.id.status)
    }

    override fun onDestroy() {
        Log.d("MyBluetoothApp", "onDistroy")
        super.onDestroy()
        bluetoothHandler.onDistroy()
    }

    private inner class ButtonClickListner() : View.OnClickListener{
        override fun onClick(v: View?) {
            val message = messageInputEditText.text.toString()
            Log.d("MyBluetoothApp", "Message: $message")
            if(bluetoothHandler.connected){
                Thread(Runnable {
                    bluetoothHandler.bluetoothSocket.outputStream.write(message.toByteArray())
                    runOnUiThread {
                        messageInputEditText.text?.clear()
                    }
                }).start()
            }
        }
    }

    private inner class BluetoothHandler(){
        private val bluetoothDeviceName = "A3"
        private val bluetoothDeviceUUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB")

        private val bluetoothAdapter: BluetoothAdapter = BluetoothAdapter.getDefaultAdapter()
        private var bluetoothBroadcastReceiver = BluetoothBroadcastReceiver()
        private lateinit var bluetoothDevice: BluetoothDevice
        lateinit var bluetoothSocket: BluetoothSocket

        var connected = false

        init{
            if(bluetoothAdapter != null){
                val bluetoothIntentFilter = IntentFilter(BluetoothAdapter.ACTION_STATE_CHANGED)
                registerReceiver(bluetoothBroadcastReceiver, bluetoothIntentFilter)
                if (bluetoothAdapter.isEnabled){
                    obtainDeviceAndConnect()
                }else{
                    val enableBtIntent = Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE)
                    startActivity(enableBtIntent)
                }
            }else{
                Log.d("MyBluetoothApp", "Bluetooth not available!")
            }
        }

        fun onDistroy(){
            if(bluetoothAdapter != null) {
                unregisterReceiver(bluetoothBroadcastReceiver)
                if (connected){
                    bluetoothSocket.inputStream.close()
                    bluetoothSocket.outputStream.close()
                    bluetoothSocket.close()
                }
            }
        }

        fun obtainDeviceAndConnect(){
            var deviceFound  = false
            val pairedDevices: Set<BluetoothDevice> = bluetoothAdapter.bondedDevices
            pairedDevices.forEach { device ->
                if (device.name == bluetoothDeviceName){
                    bluetoothDevice = device
                    Log.d("MyBluetoothApp","${device.name}:${device.address} found!")
                    deviceFound = true
                }
            }

            if(deviceFound){
                bluetoothSocket =  bluetoothDevice.createRfcommSocketToServiceRecord(bluetoothDeviceUUID)
                Thread(Runnable {
                    bluetoothAdapter.cancelDiscovery()
                    try{
                        bluetoothSocket.connect()
                        connected = true
                        runOnUiThread {
                            statusView.text = "Connected!"
                        }
                    }catch (e: IOException){
                        Log.d("MyBluetoothApp","Unable to Connect!")
                    }
                }).start()
            }
        }

        private inner class BluetoothBroadcastReceiver: BroadcastReceiver() {
            override fun onReceive(context: Context?, intent: Intent?) {
                if (intent?.action == BluetoothAdapter.ACTION_STATE_CHANGED){
                    val state = intent.getIntExtra(BluetoothAdapter.EXTRA_STATE, BluetoothAdapter.ERROR)
                    if(state == BluetoothAdapter.STATE_ON){
                        obtainDeviceAndConnect()
                    }
                }
            }
        }

    }
}