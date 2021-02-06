import { Component, OnInit } from '@angular/core';

import { Subject } from 'rxjs';
import { EventEmitterService } from 'src/app/core/services/event-emitter/event-emitter.service';
import { NoteComponent } from '../note/note.component';

@Component({
  selector: 'app-graph',
  templateUrl: './graph.component.html',
  styleUrls: ['./graph.component.scss'],
})
export class GraphComponent implements OnInit {
  center$: Subject<boolean> = new Subject();
  zoomToFit$: Subject<boolean> = new Subject();

  constructor(private eventEmitterService: EventEmitterService) {}

  ngOnInit(): void {}

  onNodeClick(event: any): void {
    this.eventEmitterService.onNoteCalled(event);
  }

}
