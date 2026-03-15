declare module "gsap-trial/SplitText" {
  export class SplitText {
    constructor(target: string | Element | Element[], config?: any);
    chars?: Element[];
    words?: Element[];
    lines?: Element[];
    revert(): void;
  }
}

declare module "gsap-trial/ScrollSmoother" {
  export class ScrollSmoother {
    static create(config?: any): ScrollSmoother;
    paused(value?: boolean): boolean | void;
    kill(): void;
  }
}
