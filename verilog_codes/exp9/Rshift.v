module Rshiftregister(input clk,input clrb,input SDR,output reg [3:0]Q);
        always @(posedge clk ) 
        if(~clrb)
                Q <= 4'b0000;
        else
                Q<={SDR,Q[3:1]};    
        
endmodule

module testbench;
        reg clk, clrb, SDR;
        wire [3:0]Q;
        Rshiftregister RS(clk, clrb, SDR, Q);
        initial clk = 0;
        always #50 clk =~clk;
        initial begin
                $dumpfile("Rshift.vcd");
                $dumpvars(0,testbench);
                clk=1;
                clrb=0;
                SDR=1;
                #100
                clrb=1;
                SDR=1;
                #150;
                SDR=0;
                #200
                $finish;
        end
endmodule