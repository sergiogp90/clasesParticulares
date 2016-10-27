package com.sguerrero.mininotasparahacer;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Leer el archivo 'last_file' con un flujo de lectura, y mostrar el nombre del archivo y
        // el contenido del mismo en los EditText que corresponda.
    }
}
