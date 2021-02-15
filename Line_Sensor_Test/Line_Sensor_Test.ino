/*
 * Team Id:          2268
 * Authors List:     Amogh Amonkar
 * Filename:         Line_Sensor_Test
 * Theme:            Ant Bot
 * Functions:        loop(),setup()
 * Global Variables: None
 */

/*Pin to take input from Right LED on the sensor*/
#define led_Right A4
/*Pin to take input from Middle LED on the sensor*/
#define led_Middle A2
/*Pin to take input from Left LED on the sensor*/
#define led_Left A0

void setup() 
{
  /*Initiating the the serial communication*/
  Serial.begin(9600);
  /*Declaring all the Input pins of the line sensor*/ 
  pinMode(led_Right,INPUT);
  pinMode(led_Middle,INPUT);
  pinMode(led_Left,INPUT);
  
  Serial.println("Left_LED\tMiddle_LED\tRight_LED");
}

void loop() 
{
  /*Taking input from the line sensor */
  int Left_LED = analogRead(led_Left);
  int Middle_LED = analogRead(led_Middle);
  int Right_LED = analogRead(led_Right);
  
  /*Printing the values taken by the line sensor*/
  Serial.print(Left_LED);
  Serial.print("\t");
  Serial.print(Middle_LED);
  Serial.print("\t");
  Serial.println(Right_LED);
  
}
