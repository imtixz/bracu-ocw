import { useEffect, useState } from "react";
import CourseCard from "../components/CourseCard";
import FilterSection from "../components/FilterSection";
import Topbar from "../components/Topbar";

interface Course {
  department: string;
  code: string;
  title: string;
  id: number;
}

export default function Home() {
  const [isLoading, setIsLoading] = useState(true);
  const [courses, setCourses] = useState<Course[]>([]);

  const [filterSelection, setFilterSelection] = useState({
    departments: {
      architecture: false,
      business: false,
      biotechnology: false,
      cse: false,
      economics: false,
      eee: false,
      english: false,
      gened: false,
      law: false,
      maths: false,
      microbiology: false,
      pharmacy: false,
      physics: false,
    },
    features: {
      assignments: false,
      books: false,
      exams: false,
      lectureVideos: false,
      practiceProblems: false,
      readings: false,
      slides: false,
    },
  });

  useEffect(() => {
    //
    async function fetchCourses() {
      const results = await fetch("http://localhost:8000/api/v1/course/");
      const courses: Course[] = await results.json();
      console.log(courses, "These are the courses");
      setCourses(courses);
      setIsLoading(false);
    }

    fetchCourses();
  }, []);

  if (isLoading) {
    return <div>Loading...</div>;
  } else {
    return (
      <div className="bg-zinc-50">
        <Topbar />
        <div className="min-h-[calc(100vh-64px)] h-full">
          <div className="flex flex-col items-center my-12 gap-y-3 mx-6 sm:mx-0">
            <p className="text-4xl">Explore OpenCourseWare</p>
            <p className="text-lg">
              Search for courses, materials & teaching resources
            </p>
            <form className="flex flex-row items-center mt-5">
              <input className="w-full sm:min-w-[512px] h-[32px] px-4 py-5 border border-gray-300 rounded-l-md shadow-md" />
              <button
                type="button"
                className="bg-emerald-600 text-white px-4 cursor-pointer py-[9px] rounded-r-md shadow-md"
              >
                Search
              </button>
            </form>
          </div>

          <div className="flex flex-col sm:flex-row mx-5 sm:mx-12">
            <div className="border-t-1 border-t-neutral-800 w-full sm:w-[384px]">
              <FilterSection />
            </div>
            <div className="w-full bg-zinc-100 flex flex-col gap-y-4 py-4 border-t-1 border-t-zinc-100">
              <div className="flex flex-row justify-between px-8">
                <p className="font-bold">COURSES</p>
                <p>
                  <span className="font-bold">{courses.length}</span> results
                </p>
              </div>
              {courses.map((course) => (
                <CourseCard
                  code={course.code}
                  title={course.title}
                  description={
                    "This is a sample hard-coded description of the course"
                  }
                  level="UNDERGRADUATE"
                  tags={["Example", "Tags"]}
                />
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }
}
