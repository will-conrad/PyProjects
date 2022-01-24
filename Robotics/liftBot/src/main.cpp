/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       willconrad                                                */
/*    Created:      Fri Jan 21 2022                                           */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Controller1          controller                    
// liftL                motor         1               
// liftR                motor         2               
// left_front           motor         3               
// left_middle          motor         11              
// left_rear            motor         12              
// right_front          motor         17              
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;

competition Competition;

float myVariable, liftSpeed, forwardSpeed, turnSpeed, leftWheels, rightWheels;
float leftV, rightV, liftV;
float stickScale = 0.85;



float lerp(float a, float b, float t) {
  return a + t * (b - a);
}

float scaleInput(float x)
{
  x = lerp(0, 100, x);
  return stickScale * pow(x, 3) + (x * (1 - stickScale));
}
void spinMotors() {
  // Spin wheels to preset velocity
  liftL.spin(forward);
  liftR.spin(forward);
  left_front.spin(forward);
  left_middle.spin(forward);
  left_rear.spin(forward);
  right_front.spin(forward);
  right_middle.spin(forward);
  right_rear.spin(forward);
}
void updateVelocity() {
  //Calculate correct wheel speeds
  int driveMode = 0; //0 = original 1 = new
  if (driveMode == 0)
  {
    leftV = Controller1.Axis3.position() + Controller1.Axis4.position();
    rightV = Controller1.Axis3.position() - Controller1.Axis4.position();
    liftV = Controller1.Axis1.position();
  }
  else
  {
    leftV = Controller1.Axis3.position();
    rightV = Controller1.Axis2.position();
    if (Controller1.ButtonUp.pressing())
    {
      liftV = 100;
    }
    else
    {
      liftV = -100;
    }
  }
  //Set velocity
  liftL.setVelocity(lerp(0, 100, liftV), percent);
  liftR.setVelocity(lerp(0, 100, liftV), percent);
  left_front.setVelocity(scaleInput(leftV), percent);
  left_middle.setVelocity(scaleInput(leftV), percent);
  left_rear.setVelocity(scaleInput(leftV), percent);
  right_front.setVelocity(scaleInput(rightV), percent);
  right_middle.setVelocity(scaleInput(rightV), percent);
  right_rear.setVelocity(scaleInput(rightV), percent);
}

// "when started" hat block
int driver_control() {
  liftL.setStopping(hold);
  liftR.setStopping(hold);
  
  left_front.setStopping(brake);
  left_middle.setStopping(brake);
  left_rear.setStopping(brake);
  right_front.setStopping(brake);
  right_middle.setStopping(brake);
  right_rear.setStopping(brake);

  while (true) {
    updateVelocity();
    spinMotors();

  
    wait(5, msec);
  }
  return 0;
}
int autonomous()
{
  return 0;
}

void VEXcode_driver_task() {
  // Start the driver control tasks....
  task drive(driver_control);

  while(Competition.isDriverControl() && Competition.isEnabled()) {this_thread::sleep_for(10);}
  drive.stop();
  return;
}

void VEXcode_auton_task() {
  // Start the auton control tasks....
  task auton(autonomous);
  while(Competition.isAutonomous() && Competition.isEnabled()) {this_thread::sleep_for(10);}
  auton.stop();
  return;
}

int main() {
  vexcodeInit();
  competition::bStopTasksBetweenModes = false;
  Competition.autonomous(VEXcode_auton_task);
  Competition.drivercontrol(VEXcode_driver_task);
}