import { WidgetType } from '@/enums'

export default {
  action: {
    undo: 'undo',
    redo: 'redo',
    flip: 'flip',
    code: 'code',
    randomize: 'Randomize',
    download: 'Download',
    downloadMultiple: 'Download multiple',
    copyCode: 'Copy',
    copied: 'Copied',
    downloading: 'Downloading',
    close: 'Close',
  },
  label: {
    wrapperShape: 'Avatar Shape',
    backgroundColor: 'Background Color',
    colors: 'colors',
  },
  widgetType: {
    [WidgetType.Face]: 'Face',
    [WidgetType.Tops]: 'Tops',
    [WidgetType.Ear]: 'Ear',
    [WidgetType.Earrings]: 'Earrings',
    [WidgetType.Eyebrows]: 'Eyebrows',
    [WidgetType.Eyes]: 'Eyes',
    [WidgetType.Nose]: 'Nose',
    [WidgetType.Glasses]: 'Glasses',
    [WidgetType.Mouth]: 'Mouth',
    [WidgetType.Beard]: 'Beard',
    [WidgetType.Clothes]: 'Clothes',
  },
  wrapperShape: {
    circle: 'Circle',
    square: 'Square',
    squircle: 'Squircle',
  },
  text: {
    codeModalTitle: 'Code',
    downloadTip: 'LONG PRESS or RIGHT CLICK to save',
    downloadMultiple: 'Download',
    downloadingMultiple: 'Downloading',
    downloadMultipleTip: 'Automatically generate avatar for you',
  },
}
