/* 
 * File:   LSM6DS33.h
 * Author: Charlie Stark
 *
 * Created on May 20, 2021, 3:43 PM
 */

#ifndef LSM6DS33_H
#define	LSM6DS33_H


// LSM6DS33 address (write bit)
#define LSM6DS33_ADDRESS    0b11010100


// LSM6DS33 registers
#define WHO_AM_I        0b00001111      // Returns 0b01101001, decimal 105

// Control registers - write to these at start
#define CTRL1_XL        0x10            // Set:
                                            // Sample rate to 1.66 kHz
                                            // Sensitivity to 2g
                                            // Filter to 100 Hz
                                            // So, 0b10000010
#define CTRL2_G         0x11            // Set:
                                            // Sample rate to 1.66 kHz
                                            // Sensitivity to 1000 dps
                                            // So, 0b10001000
#define CTRL3_C         0x12            // Set to 1

// Read registers - read these for information
#define OUT_TEMP_L      0b00100000

#define OUTX_L_XL       0b00101000


// My write bits
#define my_CTRL1_XL     0b10000010
#define my_CTRL2_G      0b10001000
#define my_CTRL3_C      0b00000100


#endif	/* LSM6DS33_H */




