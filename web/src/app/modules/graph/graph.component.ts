import { Component, OnInit } from '@angular/core';

import { Subject } from 'rxjs';

@Component({
  selector: 'app-graph',
  templateUrl: './graph.component.html',
  styleUrls: ['./graph.component.scss'],
})
export class GraphComponent implements OnInit {
  center$: Subject<boolean> = new Subject();
  zoomToFit$: Subject<boolean> = new Subject();

  constructor() {}

  ngOnInit(): void {
  }

  onNodeClick(event: any): void {
    console.log(event)
  }
}
