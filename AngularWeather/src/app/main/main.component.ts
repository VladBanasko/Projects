import { Component, OnInit } from "@angular/core";

import data from "../dataFiles/cities.json";

@Component({
  selector: "app-main",
  templateUrl: "./main.component.html",
  styleUrls: ["./main.component.css"],
})
export class MainComponent implements OnInit {
  constructor() {}

  ngOnInit(): void {
    data;
  }
}
