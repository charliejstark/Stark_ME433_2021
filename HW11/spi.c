
#include <proc/p32mx170f256b.h>
#include <xc.h>
#include "spi.h"

// initialize SPI1
void initSPI() {
    // Pin B14 has to be SCK1
    // Turn off analog pins
    ANSELA = 0;
    ANSELB = 0;
    
    // B15 -> RES (reset), initialize to High
    TRISBbits.TRISB15 = 0;
    LATBbits.LATB15   = 1;
    
    // B14 is SCK1 (output), set initially high
    TRISBbits.TRISB14 = 0;  // B14 is output
    LATBbits.LATB14   = 1;  // B14 is initially high
    
    // B13 is SD0 (output), set initially high
    //TRISBbits.TRISB13 = 0;  // B13 is output
    //LATBbits.LATB13   = 1;  // B13 is initially high
    
    // Set B12 -> DC (data control), initialize LOW
    TRISBbits.TRISB12 = 0;  // B12 is output
    LATBbits.LATB12   = 0;  // B12 is initially low
    
    
    
    // Set SDO1
    RPB13Rbits.RPB13R = 0b0011;
    
    // Set SDI1
    //SDI1Rbits.SDI1R = 0b0001;
    
    // setup SPI1
    SPI1CON = 0; // turn off the spi module and reset it
    SPI1BUF; // clear the rx buffer by reading from it
    SPI1BRG = 1; // 1000 for 24kHz, 1 for 12MHz; // baud rate to 10 MHz [SPI1BRG = (48000000/(2*desired))-1]
    SPI1STATbits.SPIROV = 0; // clear the overflow bit
    SPI1CONbits.CKP = 1;    // Clock idle high *This is specific to ST7789*
    SPI1CONbits.CKE = 1; // data changes when clock goes from hi to lo (since CKP is 0)
    SPI1CONbits.MSTEN = 1; // master operation
    SPI1CONbits.ON = 1; // turn on spi 
    
    
    LATBbits.LATB15 = 0;
    _CP0_SET_COUNT(0);
    while (_CP0_GET_COUNT() < 24000000 / 1000) {}
    LATBbits.LATB15 = 1;
    
}

unsigned char spi_io(unsigned char o) {

    SPI1BUF = o;
    
    while (!SPI1STATbits.SPIRBF) {
        ;
    }
    return SPI1BUF;

}


//void spiWrite(unsigned short c, unsigned short v) {
//       
//    unsigned short p;
//    p = (c << 15);
//    p = p | (0b111 << 12);
//    p = p | (v << 2);
//
//    LATBbits.LATB12 = 0;    // Bring CS low in order to write
//    
//    spi_io(p >> 8);
//    spi_io(p);
//    
//    LATBbits.LATB12 = 1;    // Bring CS high in order to write
//
//}




