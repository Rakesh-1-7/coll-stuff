
module addor(a,b,c,y);
    input a,b,c;
    output y;
    wire and_op1, and_op2, and_op3, and_op4, and_op5;
    and g1(and_op1,~a,~c);
    and g2(and_op2,~a,c);
    and g3(and_op3,a,~b);

    or g4(and_op4, and_op1, and_op2);
    or g5(and_op5, and_op3, and_op4);
    or g6(y, and_op5, and_op4);

endmodule

module testbench;
        reg a,b,c,d;
        wire y;
        addor ao(a,b,c,y);
        initial begin
                    $dumpfile("and_or.vcd");
                    $dumpvars(0,testbench);
                    a=0;b=0;c=0;
                     #5
                    a=0;b=0;c=1;
                     #5
                    a=0;b=1;c=0;
                     #5
                    a=0;b=1;c=1;
                     #5
                    a=1;b=0;c=0;
                     #5
                    a=1;b=0;c=1;
                     #5
                    a=1;b=1;c=0;
                     #5
                    a=1;b=1;c=1;  
                     $finish;  
        end

endmodule