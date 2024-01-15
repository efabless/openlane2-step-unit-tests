module mux(
    input A0,
    input A1,
    input S,
    output X
);
    sky130_fd_sc_hd__ebufn_2 a0 (
        .A(A0),
        .TE_B(~S),
        .Z(X)
    );
    
    sky130_fd_sc_hd__ebufn_2 a1 (
        .A(A1),
        .TE_B(S),
        .Z(X)
    );
endmodule
