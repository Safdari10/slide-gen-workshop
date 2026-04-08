import asyncio
from .planner import PlannerAgent
from .writer  import WriterAgent

class SlideOrchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.writer  = WriterAgent()

    async def run(self, prompt: str, slide_count: int = 5) -> list[dict]:
        print(f"[Orchestrator] Planning {slide_count} slides for: {prompt}")
        outline = await self.planner.run(prompt, slide_count)

        print(f"[Orchestrator] Writing {len(outline)} slides in parallel...")
        slides = await asyncio.gather(
            *[self.writer.run(item) for item in outline]
        )
        print(f"[Orchestrator] Done — {len(slides)} slides ready.")
        return list(slides)
