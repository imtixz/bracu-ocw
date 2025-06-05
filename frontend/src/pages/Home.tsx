import CourseCard from "../components/CourseCard";
import FilterSection from "../components/FilterSection";
import Topbar from "../components/Topbar";

export default function Home() {
  return (
    <div className="bg-zinc-50">
      <Topbar />
      <div className="min-h-[calc(100vh-64px)] h-full">
        <div className="flex flex-col items-center my-12 gap-y-3">
          <p className="text-4xl">Explore OpenCourseWare</p>
          <p className="text-lg">
            Search for courses, materials & teaching resources
          </p>
          <form className="flex flex-row items-center mt-5">
            <input className="min-w-[512px] h-[32px] px-4 py-5 border border-gray-300 rounded-l-md shadow-md" />
            <button
              type="button"
              className="bg-emerald-600 text-white px-4 cursor-pointer py-[9px] rounded-r-md shadow-md"
            >
              Search
            </button>
          </form>
        </div>

        <div className="flex flex-col sm:flex-row mx-12">
          <div className="border-t-1 border-t-neutral-800 w-[384px]">
            <FilterSection />
          </div>
          <div className="w-full bg-zinc-100 flex flex-col gap-y-4 py-4 border-t-1 border-t-zinc-100">
            <div className="flex flex-row justify-between px-8">
              <p className="font-bold">COURSES</p>
              <p>
                <span className="font-bold">43</span> results
              </p>
            </div>
            <CourseCard
              code="CSE330"
              title="Numerical Methods"
              description="One liner explanation of what this course is about"
              level="UNDERGRADUATE"
              tags={["Lecture Notes", "Lecture Videos", "Assignments"]}
            />
            <CourseCard
              code="CSE425"
              title="Neural Network"
              description="Learn the foundations of the most widely used AI algorithm"
              level="UNDERGRADUATE"
              tags={["Project", "Lecture Notes", "Lecture Videos", "Exams"]}
            />
            <CourseCard
              code="CSE422"
              title="Artificial Intelligence"
              description="The fundamental basics of AI algorithms"
              level="UNDERGRADUATE"
              tags={["Project", "Practice Problems", "Assignments", "Exams"]}
            />
            <CourseCard
              code="MAT101"
              title="Calculus I"
              description="Introduction to differential and integral calculus"
              level="UNDERGRADUATE"
              tags={["Lecture Notes", "Tutorials", "Assignments"]}
            />
            <CourseCard
              code="PHY201"
              title="Physics II"
              description="Electricity, magnetism, and optics"
              level="UNDERGRADUATE"
              tags={["Lecture Videos", "Lab Manuals", "Exams"]}
            />
          </div>
        </div>
      </div>
    </div>
  );
}
