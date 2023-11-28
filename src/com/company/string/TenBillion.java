package com.company.string;

import java.util.*;

public class TenBillion {

    private static String[] arr = {"a", "b", "c", "d", "a"};

    public static void main(String[] args) {
        HashSet<String> st = new HashSet<String>(List.of(arr));
        ArrayList<String> list = new ArrayList<>();

        for (String s : arr) {
            if (st.contains(s)) {
                st.remove(s);
            } else {
                list.add(s);
            }
        }
        System.out.println(list.toString());
    }
}
