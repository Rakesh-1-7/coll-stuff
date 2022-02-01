module exor(input a,b,output x);
    wire r,s,t;
    and a1(r,~a,b);
    and a2(s,a,~b);
    or o1(t,r,s);
    assign x = t;

endmodule

module NNE(a,b,t0,t1,t2);
        input a,b;
        output t0, t1, t2;
        nand n1(t0,a,b);
        nor n2(t1,a,b);
        exor e1(a,b,t2);
endmodule

module testbench;
    reg a, b;
    wire t0, t1, t2;
    NNE n(a, b,t0, t1, t2);
    initial 
    begin
        $dumpfile("NandNorExor.vcd");
        $dumpvars(0,testbench);
        a= 1'b0; b=1'b0;
        #20
        a= 1'b0; b=1'b1; 
        #20
        a= 1'b1; b=1'b0;
        #20
        a= 1'b1; b=1'b1;
        #20
        $finish;
    end
endmodule