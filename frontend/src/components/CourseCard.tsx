import Tag from "./Tag";

export default function CourseCard() {
  return (
    <div className="bg-white flex flex-col mx-8 px-5 py-6 rounded shadow-md/30">
        <p className="text-sm font-bold text-emerald-600">CSE330 | CSE</p>
        <p className="text-lg font-bold hover:underline cursor-pointer">Numerical Methods</p>
        <p>This is a one liner explanation of what this course is</p>
        <div className="flex flex-row gap-x-3 mt-3">
          <Tag name="Lecture Video" />
          <Tag name="Slides" />
          <Tag name="Practice Problems" />
        </div>
    </div>
  )
}
