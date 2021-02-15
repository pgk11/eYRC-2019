/*  Team Id:          2268
 *  Authors List:     Amogh Amonkar
 *  Filename:         Auto_Calibration_V2
 *  Theme:            Ant Bot
 *  Functions:        loop(), setup(), Stop(), Auto_Calibration(), Detect_Line()
 *  Global Variables: IR_Pin, Lower_Limit, Upper_Limit[], Midpoint[], i, j
 */

#define M_L 10                       /*Pin to control speed of Left motor of the bot*/   
#define M_R 11                       /*Pin to control speed of Right motor of the bot*/   
#define Dir1 3                       /*Pins to control direction of Left motor*/                 
#define Dir2 4     
#define Dir3 5                       /*Pins to control direction of Right motor*/  
#define Dir4 6

int IR_Pin[] = {A0, A2, A4};         /*Declaring array for taking analog input from the following pins*/
int Lower_Limit[] = {650, 650, 650}; /*Setting an array of the lower limit for the clibration*/
int Upper_Limit[] = {0, 0, 0};       /*Setting an array of the upper limit for the clibration*/
int Midpoint[] = {0, 0, 0};          /*Declaring an array of the midpoint of the upper limit and lower limit*/
int IR_Input[] = {0, 0, 0};          /*Declaring an array for storing input from the line sensor*/
unsigned int Final_Val = 0;          /*Final Value Returned by the line sensor*/
unsigned int IR_Count = 0;           /*Number of IR sensors detecting line*/
int i, j, k;                         /*Declaring the counter variables*/

/*  Function Name: Stop()
 *  Input:         None
 *  Output:        Stops the bot
 *  Logic:         Reduces the speed of both the wheels to zero
 *  Example Call:  Stop();
 */
void Stop()
{
  analogWrite(M_L,0);
  analogWrite(M_R,0);  
}

/*  Function Name: Auto_Calibrate()
 *  Input:         None
 *  Output:        Calibrates the line sensor to detect the blackl ine
 *  Logic:         1. Takes analog values on black surface
 *                 2. Finds lowest and the highest values
 *                 3. Does same procedure on a white surface
 *                 4. Calculates the mipoint from the upper and lower limit
 *  Example Call:  Auto_Calibrate()
 */
void Auto_Calibrate()
{
  for(i = 0; i < 900; i++)
  {
    for (j = 0; j <= 2; j++)
    {
      /*Takes analog input from the IR Sensor */
      IR_Input[j] = analogRead(IR_Pin[j]);

      /*Serial.print(IR_Input[j]) ;
      Serial.print(" ");
      if(j == 2)
      Serial.println(" ");*/      
          
      /*If input value from the IR Sensor is less than the lower limit value replace the lower limit by the current analog input */
      if (IR_Input[j] < Lower_Limit[j])
        Lower_Limit[j] = IR_Input[j];     

      /*If input value from the IR Sensor is greater than the upper limit value replace the uper limit by the current analog input */
      if (IR_Input[j] > Upper_Limit[j])
        Upper_Limit[j] = IR_Input[j];

    }
   
    if(i == 100)
    {
      /*Set directon of Left motor*/
      digitalWrite(Dir1,HIGH);     
      digitalWrite(Dir2,LOW);
      /*Set directon of Right motor*/
      digitalWrite(Dir3,HIGH);
      digitalWrite(Dir4,LOW);
      for(k = 0; k < 20000; k++)
      {
        analogWrite(M_L,150);
        analogWrite(M_R,150);
        //Serial.println("B");
      }

      Stop();
    }
    
    if(i == 700)
    {
      /*Set directon of Left motor*/
      digitalWrite(Dir1,LOW);     
      digitalWrite(Dir2,HIGH);
      /*Set directon of Right motor*/
      digitalWrite(Dir3,LOW);
      digitalWrite(Dir4,HIGH);
      for(k = 0; k < 20000; k++)
      {
        analogWrite(M_L,150);
        analogWrite(M_R,150);
        //Serial.println("F");
      }

      Stop();
    }    
  }
        
  for(i = 0; i <= 2; i++)
  {
    Midpoint[i] = (Lower_Limit[i] + ((Upper_Limit[i] - Lower_Limit[i]) / 2));

    /*Serial.print(Lower_Limit[i]) ;
    Serial.print(" ");
    Serial.print(Upper_Limit[i]) ;
    Serial.print(" ");      
    Serial.println(Midpoint[i]);*/   
  }     
}

/*  Function Name: Detect_Line()
 *  Input:         None
 *  Output:        Gives 10 to 30 value according to the position of the line. 
 *                 Gives 0 if no line is detected.
 *  Logic:         1. Takes analog input from the sensor
 *                 2. If the line is detected return a value according to its position
 *                 3. Else return 0
 *  Example Call:  int positon = Detect_Line()
 */
int Detect_Line()
{
    for(i = 0; i <= 2; i++)
  {
     /*Takes analog input from the IR Sensor */
     IR_Input[i] = analogRead(IR_Pin[i]);
     
     /*Serial.print(IR_Input[i]);
     Serial.print(" ");
     if(i == 3)
     Serial.print("\t");*/
     
     /*If the value of the LED is greater than midpoint it has detcted an LED */
     if(IR_Input[i] >= (Midpoint[i]))
     {
       Final_Val += (i + 1) * 10;
       IR_Count ++;
     }
  }
  
  //Serial.print(IR_Count);
  //Serial.print(" ");
  
  Final_Val /= IR_Count ;    

  if(IR_Count == 0)
  Final_Val = 0;
   
  return (Final_Val);
}

void setup() 
{
  /*Initiate the Serial communication*/
  Serial.begin(250000);

  /*Declaring all the Output pins of the motor*/ 
  pinMode(M_L,OUTPUT);
  pinMode(M_R,OUTPUT);                       
  pinMode(Dir1,OUTPUT);           
  pinMode(Dir2,OUTPUT);
  pinMode(Dir3,OUTPUT);
  pinMode(Dir4,OUTPUT);

  /*A loop for declaring the required along pins as Input pins*/
  for (i = 0; i <= 2; i++)
  {
    pinMode(IR_Pin[i], INPUT);
  }

  Auto_Calibrate();
  
}

void loop() 
{
  Serial.println(Detect_Line());

  /*Resetting the count of the IR LEDs*/
  Final_Val = 0;
  IR_Count = 0;
}
