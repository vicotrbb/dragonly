import { Injectable, EventEmitter } from '@angular/core';
import { Subscription } from 'rxjs/internal/Subscription';

@Injectable({
  providedIn: 'root',
})
export class EventEmitterService {
  invokeNote = new EventEmitter();
  noteSubscription: Subscription;

  constructor() {}

  onNoteCalled(event: any) {
    this.invokeNote.emit(event);
  }
}
