package com.example.usbdemo

import android.app.PendingIntent
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.hardware.usb.UsbDevice
import android.hardware.usb.UsbDeviceConnection
import android.hardware.usb.UsbManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.TextView
import com.felhr.usbserial.UsbSerialDevice
import com.felhr.usbserial.UsbSerialInterface
import com.google.android.material.textfield.TextInputEditText
import java.nio.charset.Charset
import java.util.*

class MainActivity : AppCompatActivity() {

    lateinit var m_usbManager: UsbManager
    var m_device: UsbDevice? = null
    var m_serial: UsbSerialDevice? = null
    var m_connection: UsbDeviceConnection? = null
    val ACTION_USB_PERMISSION = "permission"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        findViewById<TextView>(R.id.status).text = "Chassis Not Connected!"

        val sendButton = findViewById<Button>(R.id.sendButton)
        sendButton.setOnClickListener( object : View.OnClickListener{
            override fun onClick(v: View?) {
                val v = findViewById<TextInputEditText>(R.id.v).text.toString().toFloat()
                val w = findViewById<TextInputEditText>(R.id.w).text.toString().toFloat()
                send(v, w)
            }
        })

        m_usbManager = getSystemService(Context.USB_SERVICE) as UsbManager

        val filter = IntentFilter()
        filter.addAction(ACTION_USB_PERMISSION)
        filter.addAction(UsbManager.ACTION_USB_DEVICE_ATTACHED)
        filter.addAction(UsbManager.ACTION_USB_DEVICE_DETACHED)
        registerReceiver(broadcastReceiver, filter)

        startUsbConnecting()
    }

    private fun startUsbConnecting() {
        val usbDevices = m_usbManager.deviceList
        if (!usbDevices?.isEmpty()!!) {
            var done = false
            usbDevices.forEach { _, dev ->
                if (!done) {
                    val deviceVendorId: Int? = dev?.vendorId
                    val productId: Int? = dev?.productId
                    val serialNumber = dev?.serialNumber
                    if (deviceVendorId == 4292 && productId == 60000 && serialNumber == "0001") {
                        m_device = dev
                        findViewById<TextView>(R.id.status).text = "Chassis Connected!"
                        val intent: PendingIntent = PendingIntent.getBroadcast(this, 0, Intent(ACTION_USB_PERMISSION), 0)
                        m_usbManager.requestPermission(m_device, intent)
                        done = true
                    }
                }
            }
        } else {
            debugMsg("no usb device connected")
        }
    }


    private fun disconnect() {
        findViewById<TextView>(R.id.status).text = "Chassis Not Connected!"
        m_serial?.close()
        m_device = null
    }

    private val broadcastReceiver = object : BroadcastReceiver(){
        override fun onReceive(context: Context?, intent: Intent?) {
            if (intent?.action!! == ACTION_USB_PERMISSION) {
                val granted: Boolean = intent.extras!!.getBoolean(UsbManager.EXTRA_PERMISSION_GRANTED)
                if (granted) {
                    m_connection = m_usbManager.openDevice(m_device)
                    m_serial = UsbSerialDevice.createUsbSerialDevice(m_device, m_connection)
                    if (m_serial != null) {
                        if (m_serial!!.open()) {
                            m_serial!!.setBaudRate(115200)
                            m_serial!!.setDataBits(UsbSerialInterface.DATA_BITS_8)
                            m_serial!!.setStopBits(UsbSerialInterface.STOP_BITS_1)
                            m_serial!!.setParity(UsbSerialInterface.PARITY_NONE)
                            m_serial!!.setFlowControl(UsbSerialInterface.FLOW_CONTROL_OFF)
                        } else {
                            debugMsg("port not open")
                        }
                    } else {
                        debugMsg("port is null")
                    }
                } else {
                    debugMsg("permission not granted")
                }
            } else if (intent.action == UsbManager.ACTION_USB_DEVICE_ATTACHED) {
                startUsbConnecting()
            } else if (intent.action == UsbManager.ACTION_USB_DEVICE_DETACHED) {
                disconnect()
            }
        }
    }

    private fun debugMsg(msg:String){
        findViewById<TextView>(R.id.debug).text = msg
    }

    fun send(v:Float, w:Float){
        val msg = "$v,$w\r"
        debugMsg("msg: $msg")
        m_serial?.write(msg.toByteArray())
    }
}