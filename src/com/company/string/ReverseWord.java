package com.company.string;

import java.util.*;

public class ReverseWord {

    static String reverse(String str){
        StringBuilder reversed = new StringBuilder();

        char[] arr = str.toCharArray();
        for(int i = arr.length -1 ; i >= 0 ; i--){
            reversed.append(arr[i]);
        }
        return reversed.toString();
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for (int i = 0 ; i <= n ; i++){
            String str = sc.nextLine();
            System.out.println(reverse(str));
        }
        sc.close();
    }

}
