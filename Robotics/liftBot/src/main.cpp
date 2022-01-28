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
float stickScale = 0.6;



float lerp(float a, float b, float t) {
  return a + t * (b - a);
}

float scaleInput(float x)
{
  x = x / 100;
  x = stickScale * pow(x, 3) + (x * (1 - stickScale));
  return x * 90;
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
  
  leftV = scaleInput(Controller1.Axis3.position() + (Controller1.Axis4.position() * 0.8));
  rightV = scaleInput(Controller1.Axis3.position() - (Controller1.Axis4.position() * 0.8));
  liftV = -1 * Controller1.Axis2.position();
  
  // if (Controller1.ButtonR2.pressing())
  // {
  //   liftL.setVelocity(100, percent);
  //   liftR.setVelocity(100, percent);
  // }
  // else if (Controller1.ButtonR1.pressing())
  // {
  //   liftL.setVelocity(-100, percent);
  //   liftR.setVelocity(-100, percent);
  // }
  // else
  // {
  //   liftL.setVelocity(0, percent);
  //   liftR.setVelocity(0, percent);
  // }
  //Set velocity
  liftL.setVelocity(liftV, percent);
  liftR.setVelocity(liftV, percent);
  left_front.setVelocity(leftV, percent);
  left_middle.setVelocity(leftV, percent);
  left_rear.setVelocity(leftV, percent);
  right_front.setVelocity(rightV, percent);
  right_middle.setVelocity(rightV, percent);
  right_rear.setVelocity(rightV, percent);
}

// "when started" hat block
int driver_control() {
  liftL.setStopping(hold);
  liftR.setStopping(hold);
  
  left_front.setStopping(hold);
  left_middle.setStopping(hold);
  left_rear.setStopping(hold);
  right_front.setStopping(hold);
  right_middle.setStopping(hold);
  right_rear.setStopping(hold);

  while (true) {
    updateVelocity();
    spinMotors();

  
    wait(5, msec);
  }
  return 0;
}
int autonomous()
{
  int rot = 360 * 5;
  left_front.spinFor(forward, rot, degrees, true);
  left_middle.spinFor(forward, rot, degrees, true);
  left_rear.spinFor(forward, rot, degrees, true);
  right_front.spinFor(forward, rot, degrees, true);
  right_middle.spinFor(forward, rot, degrees, true);
  right_rear.spinFor(forward, rot, degrees, true);
  wait(1.0, seconds);
  //right_rear.spinFor(forward, rot, degrees, true);


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