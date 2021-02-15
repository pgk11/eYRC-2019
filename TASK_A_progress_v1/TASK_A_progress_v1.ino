/*
 * Team Id:          2268
 * Authors List:     Amogh Amonkar
 * Filename:         Motor_Test
 * Theme:            Ant Bot
 * Functions:        loop(),setup()
 * Global Variables: None
 */

/*Pin to control speed of Left motor of the bot*/
#define M_L 10 
/*Pin to control speed of Right motor of the bot*/        
#define M_R 11         
/*Pins to control direction of Left motor*/
#define Dir1 3         
#define Dir2 4     
/*Pins to control direction of Right motor*/    
#define Dir3 5         
#define Dir4 6
/*Pin to take input from Right LED on the sensor*/
#define led_Right A4
/*Pin to take input from Middle LED on the sensor*/
#define led_Middle A2
/*Pin to take input from Left LED on the sensor*/
#define led_Left A0


void setup() 
{
  /*Declaring all the Output pins of the motor*/ 
  pinMode(M_L,OUTPUT);
  pinMode(M_R,OUTPUT);                       
  pinMode(Dir1,OUTPUT);           
  pinMode(Dir2,OUTPUT);
  pinMode(Dir3,OUTPUT);
  pinMode(Dir4,OUTPUT);
  /*Declaring all the Input pins of the line sensor*/ 
  pinMode(led_Right,INPUT);
  pinMode(led_Middle,INPUT);
  pinMode(led_Left,INPUT);
  
}

void loop() 
{
  /*Set the PWM values of the the motors*/
  //int pwm_L=150 ,pwm_R=150;   
  /*Taking input from the line sensor */
  int Left_LED = analogRead(led_Left);
  int Middle_LED = analogRead(led_Middle);
  int Right_LED = analogRead(led_Right);
  int ctr = 0;
  /*Set directon of Left motor*/
  digitalWrite(Dir1,LOW);     
  digitalWrite(Dir2,HIGH);
  /*Set directon of Right motor*/
  digitalWrite(Dir3,LOW);
  digitalWrite(Dir4,HIGH);

  if(Left_LED>=200 && Middle_LED>=200 && Right_LED>=200)
  {
    ctr += 1;
  }
  if(ctr = 1)
  {
    analogWrite(M_L,150);
    analogWrite(M_R,150);
    delay(300);
  }
  if(ctr = 2)
  {
    analogWrite(M_L,150);
    analogWrite(M_R,150);
    delay(300);
  }
  if(ctr = 2)
  {
    analogWrite(M_L,0);
    analogWrite(M_R,0);
    delay(300);
  }
  /*Rotate the  motors with in given direction at and speed*/
  
}
