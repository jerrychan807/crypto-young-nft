export const enum Locale {
    ZH = 'zh',
    EN = 'en',
}

export const enum ActionType {
    Undo = 'undo',
    Redo = 'redo',
    Flip = 'flip',
    Code = 'code',
}

export enum Gender {
    Male = 'male',
    Female = 'female',
    NotSet = 'notSet',
}

export enum WidgetType {
    Face = 'face',
    Tops = 'tops',
    Ear = 'ear',
    Earrings = 'earrings',
    Eyebrows = 'eyebrows',
    Eyes = 'eyes',
    Nose = 'nose',
    Glasses = 'glasses',
    Mouth = 'mouth',
    Beard = 'beard',
    Clothes = 'clothes',
}

export enum WrapperShape {
    Circle = 'circle',
    Square = 'square',
    Squircle = 'squircle',
}

/**
 * WidgetShape
 *
 * All enumeration values of `WidgetShape` correspond to the file name.
 */

export enum FaceShape {
    Base = 'base',
}

export enum TopsShape {
    Fonze = 'fonze',
    Funny = 'funny',
    Clean = 'clean',
    Punk = 'punk',
    Danny = 'danny',
    Wave = 'wave',
    Turban = 'turban',
    Pixie = 'pixie',
    Beanie = 'beanie',
}

export enum EarShape {
    Attached = 'attached',
    Detached = 'detached',
}

export enum EarringsShape {
    Hoop = 'hoop',
    Stud = 'stud',
    None = 'none',
}

export enum EyebrowsShape {
    Up = 'up',
    Eyelashesup = 'eyelashesup',
}

export enum EyesShape {
    Ada = 'ada',
    Bnb = 'bnb',
    Btc = 'btc',
    Busd = 'busd',
    Doge = 'doge',
    Eth = 'eth',
    Sol = 'sol',
    Usdc = 'usdc',
    Usdt = 'usdt',
    Xrp = 'xrp',
}

export enum NoseShape {
    Curve = 'curve',
    Round = 'round',
    Pointed = 'pointed',
}

export enum MouthShape {
    Laughing = 'laughing',
    Pucker = 'pucker',
    Smile = 'smile',
    Smirk = 'smirk',
    Surprised = 'surprised',
}

export enum BeardShape {
    Scruff = 'scruff',
    None = 'none',
}

export enum GlassesShape {
    Round = 'round',
    Square = 'square',
    None = 'none',
}

export enum ClothesShape {
    Crew = 'crew',
    Collared = 'collared',
    Open = 'open',
}

export type WidgetShape =
    | FaceShape
    | TopsShape
    | EarShape
    | EarringsShape
    | EyebrowsShape
    | EyesShape
    | NoseShape
    | MouthShape
    | BeardShape
    | GlassesShape
    | ClothesShape
