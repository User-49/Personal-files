package com.project_2

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.project_2.ui.theme.Project_2Theme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            Project_2Theme {
                Surface(modifier = Modifier.fillMaxSize()){
                    GreetingText("Happy Birthday Dude", "Kapil", modifier= Modifier.padding(50.dp))
                }
            }
        }
    }
}

@Composable
fun GreetingText(message:String, senderName:String,  modifier:Modifier = Modifier):Unit {
    Column(modifier= modifier.padding(8.dp), verticalArrangement = Arrangement.Center) {
        Text(text = message, fontSize = 56.sp, lineHeight = 66.sp, textAlign = TextAlign.Center)
        Text(text = "from $senderName", fontSize = 36.sp, modifier=modifier.padding(4.dp).align(alignment=Alignment.End))
       }
}

@Composable
fun GreetingImage(message: String, senderName: String, modifier: Modifier= Modifier){

}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    Project_2Theme {
        GreetingText("Happy Birthday dude", "Kapil")
    }
}